from django.urls import path, include

from .views import SettlersView, SettlersPkView


app_name = 'authentication'


urlpatterns = [
    path('dormitory/<int:dormitory_pk>/settlers', SettlersView.as_view()),
    path('dormitory/<int:dormitory_pk>/settlers/<int:pk>', SettlersPkView.as_view())
]