from django.db import models


class Post(models.Model):
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

