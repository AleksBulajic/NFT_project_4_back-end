from django.shortcuts import render
from rest_framework import generics

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

from rest_framework import viewsets
from .models import User, Identity
from .serializers import UserSerializer, IdentitySerializer
from django.core.exceptions import MultipleObjectsReturned
from rest_framework.exceptions import PermissionDenied
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from .authentication import CustomTokenAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import action

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

# Create your views here.

@api_view(["POST"])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    store_token, _ = TestToken.objects.get_or_create(token=token.key, user=user)

    serializer = UserSerializer(user)

    return Response({'token': store_token.token, 'user': serializer.data})

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


# class DeletePost(APIView):
#     authentication_classes = [CustomTokenAuthentication]

#     def delete(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)

#         if post.user_id != request.user.id:
#             return Response({'error': 'You do not have permissions for this operation.'}, status=403)

#         post.delete()

#         return Response(status=204)