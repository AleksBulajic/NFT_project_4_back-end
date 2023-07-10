from django.shortcuts import render
from rest_framework import generics

from .models import User , Identity
from .serializers import UserSerializer, IdentitySerializer

# Create your views here.

class UserCreatView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class IdentityCreateView(generics.CreateAPIView):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer
