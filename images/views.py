from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Image, Text

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