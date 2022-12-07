# rest framework
from rest_framework import serializers

# directories
from .models import User

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'password']