from django.db import models
from django.conf import settings
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    reference = models.TextField(blank=True)
    published_in = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title