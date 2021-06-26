import json
from django.http import JsonResponse

import cloudinary
import cloudinary.uploader
import cloudinary.api

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.authtoken.models import Token


from .models import Image
from .serializers import UserAccountSerializer


def create_user_account(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        serializer = UserAccountSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"detail": "user account created successfully"})

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
def upload_image(request):
    """
    Uploads an image and returns related data

    * Requires authentication
    """
    try:
        source_image = request.FILES['image']
        upload = cloudinary.uploader.upload(source_image.file)

        image = Image()
        image.original_name = source_image.name
        image.public_id = upload['public_id']
        image.url = upload['url']
        image.secure_url = upload['secure_url']
        image.created_at = upload['created_at']

        token_header = request.headers['Authorization']
        user_token = str(token_header).split(' ')[1]
        user = Token.objects.get(key=user_token).user

        image.owner = user.email
        image.save()

        return Response({
            "detail": "image uploaded successfully",
            "public_id": image.public_id,
            "timestamp": image.created_at,
            "url": image.secure_url
        })
    except Exception as e:
        # raise
        return Response({
            "detail": "failed to upload image",
        })
