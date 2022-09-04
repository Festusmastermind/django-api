from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer, CustomUser, UserProfile, UserProfileSerializer

# Create your views here.

'''
    ModelViewSet...enables us to perform CRUD operation on the queryset provided..
'''

class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()