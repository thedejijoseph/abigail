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