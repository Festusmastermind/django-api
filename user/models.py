from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    # overide the create_user and create_superuser built-in method 

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email field is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        # checking for a certain property ..and sets it default just in case its not defined
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('name', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True ')
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Super must have is_superuser=True ')
        
        # create the super user
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # required fields for overiding the User class
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)


    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class AddressGlobal(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name="user_profile", on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pics")
    address_info = models.ForeignKey(AddressGlobal, related_name="user_address", null=True, on_delete=models.SET_NULL)
    dob = models.DateField()


    def __str__(self):
        return self.user.email
