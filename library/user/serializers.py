from rest_framework import serializers
from .models import User

class UserSerializator(serializers.Serializer):
    class Meta:
        model=User
        fields=['id','first_name','last_name','middle_name','email','created_at','password','role','is_active','is_superuser']