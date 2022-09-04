from tabnanny import verbose
from django.db import models
from django.utils import timezone

# Create your models here.

#OneToMany, ManyToOne relationship
#OneToOne  and ManyToMany relationship

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title 

class Car(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name


class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_alive = models.BooleanField()
    amount = models.FloatField()
    detailed_name = models.CharField(max_length=255, editable=False, default="null") # editable means it can't be edited, thus not showing on our admin page
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Note that we can the default flow of the Model itself within the Meta class, sample is below
    class Meta: 
        ordering = ("-created_at",) # the preceeding - means descending order 
        verbose_name_plural = "Test Model" # overiding the default plural of table/model name  i.e Test models to Test Model


    def __str__(self):
        return self.name
        # return f"{self.name} - {self.created_at.strftime(' %H: %M: %S')}"
        # return f"{self.detailed_name}"
        

    '''
       Note that we can specify how we want our data to be saved into the database 
       by overiding the "save" method that's called each a record want's to get saved .
    '''
 
    def save(self, *args, **kwargs):
        self.detailed_name = f"{self.name} - {self.phone_number}"
        # called the super method for the actual save. 
        super().save(*args, **kwargs)


   # test_content = models.ForeignKey(TestModel, on_delete=models.SET_NULL, null=True) this means the reference will be delete when its deleted
class ModelX(models.Model):
    test_content = models.ForeignKey(TestModel, on_delete=models.CASCADE, related_name="test_content") # for relating 
    mileage = models.FloatField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
   
    class Meta: 
        ordering = ("-created_at",)
        verbose_name_plural = "ModelX"

    def __str__ (self):
        return f"{self.test_content.name} - {self.mileage}"

'''
  A OneToOneField simply means a model can only have an instance of the other model ...
'''

class ModelY(models.Model):
    test_cont = models.OneToOneField(TestModel, on_delete=models.CASCADE, related_name="test_cont") # for relating 
    mileage = models.FloatField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
   
    class Meta: 
        ordering = ("-created_at",)
        verbose_name_plural = "ModelY"

    def __str__ (self):
        return f"{self.test_cont.name} - {self.mileage}"
        

