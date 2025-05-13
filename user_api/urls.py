from django.contrib import admin
from django.urls import path, include
# This is a sample Django URL configuration file. It includes the admin site and the API URLs.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls'))
]
