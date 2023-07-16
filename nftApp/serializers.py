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
    class Meta:
        model = Identity
        fields = [
            'id', 'user', 'firstName', 'lastName', 'photo', 'description', 'nft_token_id', 'address', 'country', 'dateOfBirth', 'eyeColor' 
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(IdentitySerializer, self).create(validated_data)
     
    def get_user(self, obj):
        return obj.user.id
    
 
class TestTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestToken
        fields = '__all__'   
