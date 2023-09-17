from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('obreplace-app/', include('core_apps.obreplace_app.api.urls')),
]
