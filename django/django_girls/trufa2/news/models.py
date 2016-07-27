from django.db import models
from django.utils import timezone

# Create your models here.

class NewsPost(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField(default="BLANK POST")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def publish(self):
        self.save()
