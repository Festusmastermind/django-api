from rest_framework import serializers
from .models import CustomUser, UserProfile, AddressGlobal






class AddressGlobalSerializer(serializers.Serializer):

    class Meta:
        model = AddressGlobal
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    address_info = AddressGlobalSerializer() # to access the address  
    # some normally..the id is been returned for the userForeignkey..
    # user = CustomUserSerializer()  # to show the serialized information about the user..
    class Meta: 
        model = UserProfile
        fields = "__all__" # all the columns are available..


class CustomUserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer() # using the related_name to have to the userprofile...
    class Meta:
        model = CustomUser
        fields = ["email", "name", "user_profile", "created_at", "updated_at"]



