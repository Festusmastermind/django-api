from rest_framework import serializers

# create the serializers 



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegiseterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    name = serializers.CharField()


class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()