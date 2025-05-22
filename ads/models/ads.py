from django.db import models
from django.contrib.auth.models import User


class ConditionChoices(models.TextChoices):
    NEW = 'new', 'Новый'
    USED = 'used', 'Б/у'


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=10, choices=ConditionChoices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
