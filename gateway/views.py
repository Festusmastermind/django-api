import jwt
import random
import string
from gateway.serializers import LoginSerializer, RefreshSerializer, RegiseterSerializer
from .authentication import Authentication
from .models import Jwt
from user.models import CustomUser
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

 

# Create your views here.

def get_random(length):
   return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_access_token(payload):
    '''
      accessToken are used to tie an information to the current logged in user..
      payload = a dictionary that contains the user details.. 
      this token expires after 5mins...
    '''
    return jwt.encode(
        {
            "exp": datetime.now() + timedelta(minutes=5), **payload
        },
        settings.SECRET_KEY,
        algorithm="HS256"
    )

def get_refresh_token():
    '''
        NB: refresh token allows the server to issue another token when the access token has expired..
    '''
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data": get_random(10) },
        settings.SECRET_KEY,
        algorithm="HS256"
    )

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['email'], 
            password=serializer.validated_data['password']
            )
        if not user: 
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # delete the existing token if there's any 
        Jwt.objects.filter(user_id = user.id).delete()
        # get accessToken and refreshToken
        access = get_access_token({"user_id": user.id})
        refresh = get_refresh_token()
        
        # saved the data into Jwt Table to tracked the login details ..
    
        Jwt.objects.create(
            user_id=user.id, access=access, refresh=refresh
        )
        return Response({"accessToken": access, "refresh": refresh})


class RegisterView(APIView):
    serializer_class = RegiseterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # CustomUser userManager allows us to create a new user 
        CustomUser.objects.create_user(**serializer.validated_data)
        
        return Response({"success": "user created successfully"})



class RefreshView(APIView):
    '''
        check to see if the refresh token is still existing 
        check to see if the token is still valid within the time frame 
        generat another accessToken and refreshToken
    '''
    serializer_class = RefreshSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            active_jwt = Jwt.objects.get(refresh=serializer.validated_data["refresh"])
        except Jwt.DoesNotExist:
            return Response({"error": "refresh token not found" }, status=status.HTTP_401_UNAUTHORIZED)
        # verify the token 
        if not Authentication.verify_token(serializer.validated_data["refresh"]):
            return Response({"error": "Token is invalid or has expired"}) 

        # generate another accessToken and refreshToken
        access = get_access_token({"user_id" : active_jwt.user.id})
        refresh = get_refresh_token()

        # active_jwt.access = access.decode()
        active_jwt.access = access
        active_jwt.refresh = refresh
        active_jwt.save()

        return Response({"access": access, "refresh": refresh})

# test authetication and authorization..
class GetSecuredInfo(APIView):
    # authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated] # this calls invokes the global authentication..

    def get(self, request):
        print("User", request.user)
        return Response({"data": "This is a a secured info"})


# handling Exception 
class TestException(APIView):

    def get(self, request):
      #  a = 2 / 0 # raises an exception ..
        # but in most cases ...we can raise the exception ourselves..
        try:
            a = 2 / 0 
        except Exception as e: 
            #raise Exception(e) #system error message..
            raise Exception("you can't divide by 0") 
        return Response("You are doing well")