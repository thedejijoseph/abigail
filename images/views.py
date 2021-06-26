import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from.serializers import UserAccountSerializer

from .models import Image, Text

def create_user_account(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        serializer = UserAccountSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"detail": "user account created successfully"})

def images_list(request):
    max_buffer = 12
    images = Image.objects.all()[:max_buffer]
    data = {"results": list(images.values("image", "username", "desc"))}
    return JsonResponse(data)

def images_details(request, pk):
    image = get_object_or_404(Image, pk=pk)
    data = {"results": {
        "image": "this should contain image's unique url",
        "user": image.username.username,
        "desc": image.desc
    }}
    return JsonResponse(data)

def text_content(request, pk):
    text = get_object_or_404(Text, pk=pk)
    data = {"results": {
        "content": text.content
    }}
    return JsonResponse(data)