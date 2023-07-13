from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Identity, TestToken

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('metamask_wallet_address',)

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'userprofile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password is not None:
            user.set_password(password)
        user.is_staff = True
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user
    
    def update(self, instance, validated_data):
        userprofile_data = validated_data.pop('userprofile', {})
        userprofile = instance.userprofile
        
        # Update user profile fields
        for key, value in userprofile_data.items():
            setattr(userprofile, key, value)
        userprofile.save()

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
        return obj.user.username
    
 
class TestTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestToken
        fields = '__all__'   
