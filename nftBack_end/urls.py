from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from nftApp.views import UserCreate, UserViewSet, IdentityListCreateView, UserRetrieveUpdateDestroyView, IdentityRetrieveUpdateDestroyView, CustomAuthToken
''
router = DefaultRouter()
router.register(r'identity', IdentityListCreateView)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register/', UserCreate.as_view(), name='user-register'),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    #  path('users/', UserViewSet.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('identities/', IdentityListCreateView.as_view(actions={'get': 'list', 'post': 'create'}), name='identity-list-create'),
    path('identities/<int:pk>/', IdentityRetrieveUpdateDestroyView.as_view(), name='identity-retrieve-update-destroy')
]
