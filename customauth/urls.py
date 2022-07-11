from django.urls import path, include
from .views import *
from knox import views as knox_views

urlpatterns = [
    # Auth views
    path('',include('knox.urls')),
    path('register', RegisterAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('user', UserAPI.as_view()),
    path('user_update', UserUpdateAPI.as_view()),
    path('change_password', ChangePasswordView.as_view(), name='auth_change_password'),
    path('logout', knox_views.LogoutView.as_view(),name='knox_logout'),
    path('reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
    
]
