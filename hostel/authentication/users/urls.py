from django.urls import path
from .views import CustomUserView


app_name = 'users'


urlpatterns = [
    path('users', CustomUserView.as_view()),
]