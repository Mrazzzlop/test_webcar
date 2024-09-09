from django.urls import path

from .views import (
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    ProfileListView,
    ProfileUpdateView,
    create_comment,
    edit_comment,
    delete_comment
)

app_name = 'car'

urlpatterns = [
    path('', CarListView.as_view(), name='index'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('profiles/<str:username>/',
         ProfileListView.as_view(),
         name='profile'
         ),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('cars/create/', CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/edit/', CarUpdateView.as_view(), name='car_edit'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    path('cars/<int:car_id>/comments/', create_comment, name='create_comment'),
    path(
        'cars/<int:car_id>/comments/<int:comment_id>/edit/',
        edit_comment,
        name='edit_comment'
    ),
    path(
        'cars/<int:car_id>/comments/<int:comment_id>/delete/',
        delete_comment,
        name='delete_comment'
    ),
]
