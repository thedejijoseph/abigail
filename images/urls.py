from django.urls import path

from rest_framework.authtoken import views as authtoken_views

from .views import create_user_account

urlpatterns = [
    path("create-account", create_user_account, name="create_account"),
]

urlpatterns += [
    path('obtain-auth-token', authtoken_views.obtain_auth_token)
]