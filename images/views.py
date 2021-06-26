import json
from django.http import JsonResponse

from.serializers import UserAccountSerializer


def create_user_account(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        serializer = UserAccountSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"detail": "user account created successfully"})
