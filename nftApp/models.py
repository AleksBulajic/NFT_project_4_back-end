from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class Identity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    eye_color = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName

class TestToken(models.Model):
    token = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.token