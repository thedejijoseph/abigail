from django.urls import path

from rest_framework.authtoken import views as authtoken_views

from .views import create_user_account, upload_image, index

urlpatterns = [
    path("", index, name="root"),
    path("create-account", create_user_account, name="create_account"),
    path("upload-image", upload_image, name="upload-image"),
]

urlpatterns += [
    path('obtain-auth-token', authtoken_views.obtain_auth_token)
]