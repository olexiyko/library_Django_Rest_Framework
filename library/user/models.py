from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
import datetime

ROLE_CHOICES = (
    (0, "visitor"),
    (1, "librarian"),
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)   
         
# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)
    middle_name = models.CharField(max_length=20, default=None)
    email = models.EmailField(max_length=50, unique=True, default=None)
    password = models.CharField(max_length=128, default=None)
    created_at = models.DateTimeField(auto_now=datetime.datetime.now(), editable=False)
    last_login = models.DateTimeField(auto_now=datetime.datetime.now())
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects=CustomUserManager()

    def __str__(self):
        """
        Magic method is redefined to show all information about CustomUser.
        :return: user id, user first_name, user middle_name, user last_name,
                 user email, user password, user updated_at, user created_at,
                 user role, user is_active
        """
        return f"'id': {self.id}, 'first_name': '{self.first_name}', 'middle_name': '{self.middle_name}', 'last_name': '{self.last_name}', 'email': '{self.email}', 'created_at': {int(self.created_at.timestamp())}, 'updated_at': {int(self.updated_at.timestamp())}, 'role': {self.role}, 'is_active': {self.is_active}"  # 'password': '{self.password}', \

    # def create(self,first_name,last_name,middle_name,email,password,role,is_active,is_superuser):
    #     if len(first_name) <= 20 and len(middle_name) <= 20 and len(last_name) <= 20 and len(email) <= 100 and len(
    #             email.split('@')) == 2 and len(User.objects.filter(email=email)) == 0:
    #         user = User(email=email, password=password, first_name=first_name, middle_name=middle_name,
    #                                  last_name=last_name,role=role,is_active=is_active,is_superuser=is_superuser)
    #         user.save()
    #         return user
    #     return None



        
