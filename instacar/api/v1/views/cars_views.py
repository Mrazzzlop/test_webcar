from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cars.models import Car, Comment
from api.v1.serializers.cars_serializers import (
    CarsSerializer, CommentsSerializer,
    CreateCarsSerializer, CreateCommentSerializer,
)
from api.v1.permissions import IsAdminOrAuthor


class CarViewSet(viewsets.ModelViewSet):
    """API для управления автомобилями."""
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == ('POST', 'PUT', 'DELETE',):
            return CreateCarsSerializer
        return CarsSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            self.permission_classes = (IsAdminOrAuthor,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """API для управления комментариями к автомобилям."""
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == ['POST', 'PUT', 'DELETE']:
            return CreateCommentSerializer
        return CommentsSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            self.permission_classes = (IsAdminOrAuthor,)
        return super().get_permissions()

    def get_queryset(self):
        car_id = self.kwargs['car_id']
        return Comment.objects.filter(car_id=car_id)

    def perform_create(self, serializer):
        car_id = self.kwargs['car_id']
        serializer.save(author=self.request.user, car_id=car_id)
