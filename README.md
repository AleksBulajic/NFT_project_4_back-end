# NFT_project_4_back-end

# NFT Backend System

This repository outlines a back-end system developed using Django for a Non-Fungible Token (NFT) application. The system makes use of Django REST Framework for creating REST APIs and interfaces with a frontend application.

## Features

The backend system supports the following features:

- User Registration and Authentication
- CRUD operations for Users and NFT identities
- Token-based authentication

## Models

The application defines two Django models: `UserProfile` and `Identity`. 

- `UserProfile` extends the standard `User` model provided by Django's authentication system, adding an additional `metamask_wallet_address` field. 

- `Identity` is a more complex model, containing fields for NFT related data like `firstName`, `lastName`, `photo`, `description`, `nft_token_id`, `address`, `country`, `dateOfBirth`, and `eyeColor`.

## Serializers

The Django REST Framework serializers handle conversion to and from JSON for the models.

- `UserProfileSerializer` and `IdentitySerializer` handle UserProfile and Identity models, respectively.

- `UserSerializer` converts `User` objects to and from JSON and also includes nested UserProfile objects. During creation, the `UserSerializer` also handles the task of creating a corresponding `UserProfile` for each new `User`.

## Views

The application includes several views to handle different types of HTTP requests:

- `UserCreate`: Allows new users to register.
- `CustomAuthToken`: Authenticates users and provides a token for subsequent authenticated requests.
- `UserViewSet`: Provides a list of all users, as well as user detail views.
- `UserRetrieveUpdateDestroyView`: Allows retrieving, updating, and deleting specific users.
- `IdentityListCreateView`: Provides a list of all identities, as well as identity creation views.
- `IdentityRetrieveUpdateDestroyView`: Allows retrieving, updating, and deleting specific identities.

## URL Configuration

The application's URL configuration (`urlpatterns`) sets up the URL routes for the above views, as well as some other built-in interfaces like the Django admin.

## Settings

The settings module contains application configurations, including database configurations, installed apps, middleware, URL configuration, template engine configuration, and more. It also manages static files and environment variables, and includes a configuration for token-based authentication using Django Rest Framework.

## Middleware

The middleware configuration includes Django's built-in middleware and 'whitenoise' middleware for handling static files.

## Installed Apps

The application includes several installed apps, which are:

- Django Rest Framework for REST APIs
- CORS headers for handling Cross-Origin Resource Sharing (CORS)
- 'nftApp' for this project

## Conclusion

This repository provides a comprehensive back-end system for an NFT application, built with Django and Django REST Framework. It supports user registration, user authentication, and CRUD operations for users and NFT identities.