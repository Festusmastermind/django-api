from django.urls import path, include
from .views import Simple, SimpleGenerics, SimpleGenericsUpdate
from rest_framework.routers import DefaultRouter
from .views import SimpleViewSet



# DefaultRouter allows urls to be register and generated 
router=DefaultRouter()
router.register("simple-viewset", SimpleViewSet) # entry point...


urlpatterns = [
    path('', include(router.urls)),
   # path('', Simple.as_view()),
    path('simple/<int:pk>', Simple.as_view()),
    path('simple-generics', SimpleGenerics.as_view()),
    path('simple-generics/<int:id>', SimpleGenericsUpdate.as_view()),
]

