from django.db import models
from django.utils import timezone


class Image(models.Model):
    original_filename = models.CharField(max_length=256)
    public_id = models.CharField(max_length=256)
    url = models.URLField()
    secure_url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    owner = models.EmailField()
