from django.urls import path

from rest_framework.authtoken import views as authtoken_views

from .views import images_list, images_details, text_content, create_user_account
from .apiviews import TextList, TextDetail

urlpatterns = [
    path("create-account", create_user_account, name="create_account"),
    path("images/", images_list, name="images_list"),
    path("images/<int:pk>/", images_details, name="images_details"),
    path("texts/", TextList.as_view(), name="text_list"),
    path("texts/<int:pk>/", TextDetail.as_view(), name="text_content")
]

urlpatterns += [
    path('obtain-auth-token', authtoken_views.obtain_auth_token)
]