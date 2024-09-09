from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.db.models import Count
from django.contrib import messages

from .models import Car, Comment
from .forms import CarForm, CommentForm, ProfileEditForm
from users.models import UserProfile


class CarListView(ListView):
    """Выводит главную страницу со списком автомобилей"""
    model = Car
    template_name = 'blog/index.html'
    ordering = '-created_at'
    paginate_by = 5

    def get_queryset(self):
        return (Car.objects.select_related('owner')
                .annotate(comment_count=Count('comments'))
                .order_by('-created_at'))


class CarDetailView(DetailView):
    """Выводит страницу с информацией о конкретном автомобиле"""
    model = Car
    template_name = 'blog/detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()  # Используем related_name
        context['form'] = CommentForm()
        return context


class CarCreateView(LoginRequiredMixin, CreateView):
    """Создание нового автомобиля"""
    model = Car
    form_class = CarForm
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Автомобиль успешно создан!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car:index')


class CarUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование автомобиля"""
    model = Car
    form_class = CarForm
    template_name = 'blog/create.html'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Автомобиль успешно обновлён!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car:car_detail', args=[self.object.pk])


class CarDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление автомобиля"""
    model = Car
    template_name = 'blog/confirm_delete.html'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def get_success_url(self):
        messages.success(self.request, "Автомобиль успешно удалён!")
        return reverse('car:index')


class ProfileListView(ListView):
    """Страница профиля пользователя"""
    model = Car
    template_name = 'blog/profile.html'
    paginate_by = 5

    def get_queryset(self):
        self.user_profile = get_object_or_404(
            UserProfile, username=self.kwargs['username']
        )
        return Car.objects.filter(owner=self.user_profile).annotate(
            comment_count=Count('comments')
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.user_profile
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Страница редактирования профиля"""
    model = UserProfile
    form_class = ProfileEditForm
    template_name = 'blog/user.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, "Профиль успешно обновлён!")
        return reverse('car:profile', args=(self.request.user.username,))


@login_required
def create_comment(request, car_id):
    """Создание комментария"""
    car = get_object_or_404(Car, pk=car_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.car = car
        comment.save()
    return redirect('car:car_detail', pk=car_id)


@login_required
def edit_comment(request, car_id, comment_id):
    """Редактирование комментария"""
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid() and comment.author == request.user:
            form.save()
            return redirect('car:car_detail', pk=car_id)
    else:
        form = CommentForm(instance=comment)
    return render(
        request, 'blog/comment.html', {'form': form}
    )


@login_required
def delete_comment(request, car_id, comment_id):
    """Удаление комментария"""
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST' and comment.author == request.user:
        comment.delete()
        return redirect('car:car_detail', pk=car_id)
    else:
        form = CommentForm(instance=comment)
    return render(
        request, 'blog/comment.html', {'form': form}
    )
