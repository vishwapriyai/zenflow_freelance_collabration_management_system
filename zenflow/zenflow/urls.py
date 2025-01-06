# zenflow/urls.py

from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api-token-auth/', include('rest_framework.urls')),  # This line includes the default auth views
    path('', views.home, name='home'),  # This line handles the root URL
]