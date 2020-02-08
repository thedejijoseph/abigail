from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Image, Text
from .serializers import TextSerializer

class TextList(generics.ListCreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

class TextDetail(generics.RetrieveAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer