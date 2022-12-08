from django.urls import path, include

from .views import StudentsView, StudentsPkView


app_name = 'authentication'


urlpatterns = [
    path('dormitory/<int:dormitory_pk>/students', StudentsView.as_view()),
    path('dormitory/<int:dormitory_pk>/students/<int:pk>', StudentsPkView.as_view())
]