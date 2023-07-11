"""
URL configuration for nftBack_end project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from nftApp import views



from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r'users', views.UserListCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('identities/', views.IdentityListCreateView.as_view(), name='identity-list-create'),
    path('identities/<int:pk>/', views.IdentityRetrieveUpdateDestroyView.as_view(), name='identity-retrieve-update-destroy'),
    path('', include(router.urls)),
    path('login/', views.login),
    path('signup/', views.signup)
]

