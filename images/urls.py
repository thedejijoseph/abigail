from django.urls import path

from .views import images_list, images_details, text_content
from .apiviews import TextList, TextDetail

urlpatterns = [
    path("images/", images_list, name="images_list"),
    path("images/<int:pk>/", images_details, name="images_details"),
    path("texts/", TextList.as_view(), name="text_list"),
    path("texts/<int:pk>/", TextDetail.as_view(), name="text_content")
]
