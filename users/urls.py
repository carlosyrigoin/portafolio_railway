from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from .views import RegisterView, profile

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('logout/', logout_then_login, name='logout')
]