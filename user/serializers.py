from rest_framework import serializers
from .models import CustomUser, UserProfile





class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["email", "name", "created_at", "updated_at"]


class UserProfileSerializer(serializers.ModelSerializer):
    # some normally..the id is been returned for the userForeignkey..
    user = CustomUserSerializer()  # to show the serialized information about the user..

    class Meta: 
        model = UserProfile
        fields = "__all__" # all the columns are available..
