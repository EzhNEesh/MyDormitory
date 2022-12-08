from django.urls import path, include

from .views import DormitoryView, DormitoryPkView


app_name = 'authentication'


urlpatterns = [
    path('dormitory', DormitoryView.as_view()),
    path('dormitory/<int:pk>', DormitoryPkView.as_view())
]