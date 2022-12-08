from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('users.urls')),
    path('api/', include('authentication.urls')),
    path('api/', include('dormitory.urls')),
    path('api/', include('rooms.urls')),
    path('api/', include('settlers.urls')),
    path('api/', include('students.urls'))
]
