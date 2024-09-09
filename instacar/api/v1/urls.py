from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.views.cars_views import CarViewSet
from api.v1.views.cars_views import CommentViewSet
from api.v1.views.users_views import UserViewSet

v1_router = DefaultRouter()
v1_router.register(r'cars', CarViewSet, basename='cars')
v1_router.register(r'users', UserViewSet, basename='users')

comments_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

comments_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', include(v1_router.urls)),
    path('cars/<int:car_id>/comments/', comments_list, name='car-comments'),
    path('cars/<int:car_id>/comments/<int:pk>/',
         comments_detail, name='car-comment-detail'),
    path("auth/", include('djoser.urls')),
]
