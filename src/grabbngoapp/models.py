from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Resturent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("grabbngoapp:detail", kwargs={"pk":self.pk})    