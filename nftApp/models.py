from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    metamask_wallet_address = models.CharField(max_length=255)
    # Identity = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username


class Identity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    description = models.TextField()
    nft_token_id = models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=255)
    dateOfBirth = models.CharField(max_length=255)
    eyeColor = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName

class TestToken(models.Model):
    token = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.token