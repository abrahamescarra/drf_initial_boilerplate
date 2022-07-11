from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework import routers

# Api router
router = routers.DefaultRouter()

urlpatterns = [
    # Admin routes
    path('admin/', admin.site.urls),
    # Api routes
    path('api/', include('content.urls')),
    path('auth/', include('customauth.urls')),
    #path('reportes/',include('content.urls2'))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)