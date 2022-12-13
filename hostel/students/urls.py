from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import StudentsView, StudentsPkView


app_name = 'authentication'


urlpatterns = [
    path('dormitory/<int:dormitory_pk>/students', StudentsView.as_view()),
    path('dormitory/<int:dormitory_pk>/students/<int:pk>', StudentsPkView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)