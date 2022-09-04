from doctest import testmod
from unicodedata import name
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from .models import * 
from django_seed import Seed
from .serializers import SimpleSerializer
from rest_framework import viewsets
from random import randint

# Create your views here. Choose the kind of View you want to use based on the type of operation you want to perform..

car_names = ("Mercedes", "Toyota", "Nissan", "Masarati", "honda", )



# Seeding your DB_tables programmactically
seeder = Seed.seeder()
#seeder.add_entity(Blog, 10) # Add a specific table with the number of contents to be generated
seeder.add_entity(Car, 10, {
    'name': lambda x: car_names[randint(0, len(car_names) - 1)]
})

def execute():
    '''
        Call this function inside the python shell..
    '''
    seeder.execute() 
    print("Seeding Completed") 

class SimpleViewSet(viewsets.ModelViewSet):
    '''
        This is a very powerfull class that allows Crud..with a just two lines of code ..
        NB: viewset allows us to perform GET, POST, PUT, PATCH, DELETE, HEAD...
    '''
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer


class Simple(APIView):
    '''
        APIView gives us access to overrides the basic httpRequest methods...
    '''
    def post(self, request):
        serializer_class = SimpleSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True) # using the serializer class to validate the incoming data before creating a new instance
        serializer_class.save()
        return JsonResponse({"data": serializer_class.data})
       # return JsonResponse({"data": model_to_dict(new_test_content)})
       
    def get(self, request):
        content = TestModel.objects.all()
        serializer_class = SimpleSerializer(content, many=True)
        return JsonResponse({"data": serializer_class.data})
    
    # args - non keyword argument 
    # kwargs - keyword argument.. 
    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None) # incase the id is not specified, it can use None...
        if not model_id: 
            return JsonResponse({"error": "method /PUT/ not allowed"})
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Object does not exist"})
        
        serializer = SimpleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})


class SimpleGenerics(generics.ListCreateAPIView):
    '''
        NB: ListCreateApiView Expects a queryset to work with 
        Plus its allows you to fetch all records and Create a new record 
    '''
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer

class SimpleGenericsUpdate(generics.UpdateAPIView):
    '''
        NB: UpdateAPIView allows expects a queryset and automatically looks out for an id 
    '''
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer 
    lookup_field = "id"

