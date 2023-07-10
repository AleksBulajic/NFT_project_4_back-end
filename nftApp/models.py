from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    verify_password = models.CharField(max_length=128)
    wallet_address = models.CharField(max_length=255) 

    # Add a unique related_name for groups field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
    )

    # Add a unique related_name for user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
    )

    def clean(self):
        super().clean()
        if self.password != self.verify_password:
            raise ValidationError("Password and Verify Password fields must match.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Identity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='identity_photos/')
    description = models.TextField()
    nft_token_id = models.CharField(max_length=255)

    def __str__(self):
        return self.name
