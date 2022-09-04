from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import CustomUserView, UserProfileView


# register your routes 

router = DefaultRouter()
router.register("user", CustomUserView)
router.register("user-profile", UserProfileView)

urlpatterns = [
    path("", include(router.urls))
]