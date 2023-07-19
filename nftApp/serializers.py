from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Identity, TestToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password is not None:
            user.set_password(password)
        user.is_staff = True
        user.save()
        return user

    def update(self, instance, validated_data):
        # Update user fields
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance


class IdentitySerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    photo = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    country = serializers.CharField(required=False, allow_blank=True)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    eye_color = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Identity
        fields = [
            'id', 'user', 'first_name', 'last_name', 'photo', 'description', 'address', 'country', 'date_of_birth', 'eye_color'
        ]
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
 
class TestTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestToken
        fields = '__all__'   
