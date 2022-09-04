from django.urls import path, include 
from .views import LoginView, RegisterView, RefreshView, GetSecuredInfo, TestException

urlpatterns = [
    path("login", LoginView.as_view()),
    path("register", RegisterView.as_view()),
    path("refresh", RefreshView.as_view()),
    path('secureinfo', GetSecuredInfo.as_view()),
    path('test-exec', TestException.as_view()),
]