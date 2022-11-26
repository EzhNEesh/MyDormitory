from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

#from .views import AuthUser
from .views import MyTokenObtainPairView


app_name = 'authentication'


urlpatterns = [
    path('auth', MyTokenObtainPairView.as_view()),
    path('auth/refresh', TokenRefreshView.as_view()),
    path('auth/', include('authentication.users.urls'))
    #path('users/<int:pk>', AuthUser.as_view())
]