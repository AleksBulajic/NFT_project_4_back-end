from rest_framework import serializers
from .models import User, Identity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identity
        fields = '__all__'
        
    def update(self, instance, validated_data):
        validated_data.pop('password', None)
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        validated_data['handle'] = '@' + validated_data['handle']
        return super(IdentitySerializer, self).create(validated_data)
