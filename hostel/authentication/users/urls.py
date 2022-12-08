from django.urls import path
from .views import CustomUserView


app_name = 'users'


urlpatterns = [
    path('users', CustomUserView.as_view()),
    path('users/<int:pk>', CustomUserView.as_view()),
]