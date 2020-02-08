from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return "No description." if self.desc == "" else self.desc

class Text(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content[:20]