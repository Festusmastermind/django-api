from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer, CustomUser, UserProfile, UserProfileSerializer

# Create your views here.

'''
    ModelViewSet...enables us to perform CRUD operation on the queryset provided..
'''

class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.prefetch_related("user_profile", "user_proflile_address_info") # for reverse table connection.. 


class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    #queryset = UserProfile.objects.all()
    queryset = UserProfile.objects.select_related("user", "address_info") # for faster query performance using the direct reference i.e. using Left outer join and so on..