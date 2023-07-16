from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter # this line below this one was cancelled out
#from nftApp.views import UserCreate, UserViewSet, IdentityListCreateView, UserRetrieveUpdateDestroyView, IdentityRetrieveUpdateDestroyView, CustomAuthToken, TestTokenViewSet
from nftApp.views import *
router = DefaultRouter()
router.register(r'identity', IdentityListCreateView)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register/', UserCreate.as_view(), name='user-register'),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    path('test-token/',test_token),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('identities/', IdentityListCreateView.as_view(actions={'get': 'list', 'post': 'create'}), name='identity-list-create'),
    path('identity/<int:pk>/', IdentityRetrieveUpdateDestroyView.as_view(), name='identity-retrieve-update-destroy')
]
