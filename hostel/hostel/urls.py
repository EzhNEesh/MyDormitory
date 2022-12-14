from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('users.urls')),
    path('api/', include('authentication.urls')),
    path('api/', include('dormitory.urls')),
    path('api/', include('rooms.urls')),
    path('api/', include('settlers.urls')),
    path('api/', include('students.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
