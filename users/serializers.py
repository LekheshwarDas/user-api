from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
# This serializer converts the User model instances to JSON format and vice versa.
# It includes all fields of the User model.