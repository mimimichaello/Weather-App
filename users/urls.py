from django.urls import path

from .views import RegisterView, LoginView

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LoginView.as_view(), name='logout'),
]
