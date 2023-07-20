# Import necessary modules from Django
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Define the Identity model that represents identity information for users
class Identity(models.Model):
    # Define a ForeignKey field that links the Identity model to the User model
    # on_delete=models.CASCADE specifies that if a user is deleted, their corresponding identity will also be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Define various fields to store identity information for users
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    eye_color = models.CharField(max_length=255)

    # Define a __str__ method that returns a string representation of the Identity object
    def __str__(self):
        # Return the first name of the identity as the string representation
        # This will be useful for displaying meaningful information in the Django admin interface
        return self.first_name

# Define the TestToken model that stores authentication tokens for users
class TestToken(models.Model):
    # Define a CharField to store the authentication token
    # max_length specifies the maximum length of the token string
    token = models.CharField(max_length=500)

    # Define a OneToOneField that links the TestToken model to the User model
    # on_delete=models.CASCADE specifies that if a user is deleted, their corresponding token will also be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Define a __str__ method that returns a string representation of the TestToken object
    def __str__(self):
        # Return the authentication token as the string representation
        # This will be useful for displaying meaningful information in the Django admin interface
        return self.token


