from django.shortcuts import render
from rest_framework import generics

from .models import User , Identity
from .serializers import UserSerializer, IdentitySerializer

# Create your views here.

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class IdentityListCreateView(generics.ListCreateAPIView):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer

class IdentityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer
