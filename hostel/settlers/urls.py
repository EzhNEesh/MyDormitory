from django.urls import path, include

from .views import SettlersView


app_name = 'authentication'


urlpatterns = [
    path('dormitory/<int:dormitory_pk>/settlers', SettlersView.as_view()),
    path('dormitory/<int:dormitory_pk>/settlers/<int:pk>', SettlersView.as_view())
]