# Import necessary modules from Django REST framework and Django's User model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Identity, TestToken

# Define a serializer class for the User model
class UserSerializer(serializers.ModelSerializer):
    # Meta class defines the model and fields for the serializer
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # Override the create method to handle user creation
    def create(self, validated_data):
        # Extract the 'password' field from the validated_data
        password = validated_data.pop('password', None)
        # Create a new User instance with the remaining validated_data
        user = User(**validated_data)
        # Set the password for the user using the set_password method
        if password is not None:
            user.set_password(password)
        # Set the 'is_staff' attribute of the user to True (you can customize this as per your requirements)
        user.is_staff = True
        # Save the user object to the database
        user.save()
        # Return the user object
        return user

    # Override the update method to handle user updates
    def update(self, instance, validated_data):
        # Update user fields with the validated_data
        for key, value in validated_data.items():
            setattr(instance, key, value)
        # Save the updated user object to the database
        instance.save()
        # Return the updated user object
        return instance


# Define a serializer class for the Identity model
class IdentitySerializer(serializers.ModelSerializer):
    # Define serializers for each field in the model
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    photo = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    country = serializers.CharField(required=False, allow_blank=True)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    eye_color = serializers.CharField(required=False, allow_blank=True)

    # Meta class defines the model and fields for the serializer
    class Meta:
        model = Identity
        fields = [
            'id', 'user', 'first_name', 'last_name', 'photo', 'description', 'address', 'country', 'date_of_birth', 'eye_color'
        ]

    # Override the create method to handle identity creation
    def create(self, validated_data):
        # Set the 'user' field in the validated_data to the authenticated user making the request
        validated_data['user'] = self.context['request'].user
        # Call the parent class's create method to create the Identity object in the database
        return super().create(validated_data)

    # Override the update method to handle identity updates
    def update(self, instance, validated_data):
        # Update identity fields with the validated_data
        for key, value in validated_data.items():
            setattr(instance, key, value)
        # Save the updated identity object to the database
        instance.save()
        # Return the updated identity object
        return instance


# Define a serializer class for the TestToken model
class TestTokenSerializer(serializers.ModelSerializer):
    # Meta class defines the model and fields for the serializer
    class Meta:
        model = TestToken
        fields = '__all__'
