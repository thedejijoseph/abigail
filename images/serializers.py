
from django.contrib.auth.models import User

from rest_framework import serializers


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "password")
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
