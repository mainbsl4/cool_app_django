
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todoApp.urls')),
    path('api/', include('todoApp2.urls')),
    path('api/', include('accounts.urls')),
]
