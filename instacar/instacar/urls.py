from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.edit import CreateView

from cars.forms import ProfileForm

urlpatterns = [
    path('', include('cars.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=ProfileForm,
            success_url=reverse_lazy('login')
        ),
        name='registration'
    ),
    path('api/', include('api.v1.urls')),
]
