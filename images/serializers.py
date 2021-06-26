
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Image, Text

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "password")
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
