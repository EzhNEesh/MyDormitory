from django.urls import path, include

from .views import RoomsView, RoomsPkView


app_name = 'authentication'


urlpatterns = [
    path('dormitory/<int:dormitory_pk>/rooms', RoomsView.as_view()),
    path('dormitory/<int:dormitory_pk>/rooms/<int:pk>', RoomsPkView.as_view())
]