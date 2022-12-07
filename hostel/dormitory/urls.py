from django.urls import path, include

from .views import DormitoryView


app_name = 'authentication'


urlpatterns = [
    path('dormitory', DormitoryView.as_view()),
    path('dormitory/<int:pk>', DormitoryView.as_view())
]