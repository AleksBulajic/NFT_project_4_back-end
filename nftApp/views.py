from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Identity, TestToken
from .serializers import UserSerializer, IdentitySerializer, TestTokenSerializer
from django.http import HttpResponse
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes

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
        
        user_serializer = UserSerializer(user)
        serialized_user = user_serializer.data
        
        return Response({
            'token': token.key,
            'user': serialized_user,
            'email': user.email
        }, status=HTTP_200_OK)
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def identity(self, request, pk=None):
        user = self.get_object()
        identity = Identity.objects.filter(user=user)
        serializer = Identity(identity, many=True)
        return Response(serializer.data)
    
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class IdentityListCreateView(viewsets.ModelViewSet):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        # Get the ID from the headers
        identity_id = self.request.META.get("HTTP_X_IDENTITY_ID")
        # Set the ID in the serializer's context
        serializer.context["identity_id"] = identity_id
        # Call the serializer's save method
        serializer.save(user=self.request.user)
    
class IdentityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IdentitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.kwargs['user']
        return Identity.objects.filter(user=user)
    



class TestTokenViewSet(viewsets.ModelViewSet):
    queryset = TestToken.objects.all()
    serializer_class = TestTokenSerializer
# Create your views here.
@api_view(["POST"])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    store_token, _ = TestToken.objects.get_or_create(token=token.key, user=user)

    user_serializer = UserSerializer(user)
    serialized_user = user_serializer.data

    return Response({'token': store_token.token, 'user': serialized_user})
@api_view(["POST"])
def signup(request):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': serializer.data})
      return Response(serializer.errors, status=400)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")