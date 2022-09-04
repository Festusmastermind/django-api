import jwt
from django.conf import settings
from datetime import datetime
from rest_framework.authentication import BaseAuthentication
from user.models import CustomUser



class Authentication(BaseAuthentication):


    def authenticate(self, request):
        data = self.validate_request(request.headers)
        if not data:
            return None, None
        return self.get_user(data["user_id"]), None

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            return user
        except Exception:
            return None

    def validate_request(self, headers):
        # get allows us to get the keyword value ...if not present, pass None
        authorization = headers.get("Authorization", None)
        if not authorization:
            return None
        token = headers['Authorization'][7:]  # extracting the token out from the headers 
        decoded_data = self.verify_token(token)

        if not decoded_data:
            return None
        return decoded_data

    @staticmethod # makes it accessible wihout creating a new class of authenitication
    def verify_token(token):
        # decode the token irrespective if it's access_token or refresh_token
        try: 
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256") 
            print("Decoded", decoded_data)
        except Exception: 
            return None   # i.e token is invalid..
        # check if token has expired 
        exp = decoded_data["exp"]
        if datetime.now().timestamp() > exp:
            return None
        return decoded_data