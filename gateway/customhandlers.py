from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status



'''
    Writing our own custom error handler ...helps in showing the appropriate errors in postman...
'''

def custom_exception_handler(exc, context):
    
    response = exception_handler(exc, context)
    if response is not None: 
        return response
    exc_list = str(exc).split("DETAIL: ") # we get an array that includes DETAIL in some cases 
    # returns the last element in the array...
    return Response({"error": exc_list[-1]}, status=status.HTTP_403_FORBIDDEN)
