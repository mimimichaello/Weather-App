from django.db import models

from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=255)

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.city}'
