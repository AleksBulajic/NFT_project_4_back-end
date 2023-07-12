from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Identity
from .serializers import UserSerializer, IdentitySerializer, UserProfileSerializer
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ ]
    
    def perform_create(self, serializer):
        user = serializer.save()
        # Create a token for the new user and save it
        Token.objects.create(user=user)
    
    
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def identity(self, request, pk=None):
        user = self.get_object()
        donations = Identity.objects.filter(user=user)
        serializer = Identity(donations, many=True)
        return Response(serializer.data)
    
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class IdentityListCreateView(viewsets.ModelViewSet):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer
    permission_classes = [IsAuthenticated]
    
class IdentityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer
    permission_classes = [IsAuthenticated]
