from rest_framework import serializers
from .models import CustomUser

class UserSerializator(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','first_name','last_name','middle_name','email','created_at','password','role','is_active','is_superuser']