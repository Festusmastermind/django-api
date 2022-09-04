from django.contrib import admin
from .models import TestModel, ModelX, ModelY, Blog, Car
# Register your models here.

admin.site.register((TestModel, ModelX, ModelY))
admin.site.register((Blog, Car, ))