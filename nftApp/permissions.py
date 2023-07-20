# Import the necessary module from Django REST framework
from rest_framework import permissions

# Define a custom permission class named IsAuthenticatedAndIsOwner that inherits from permissions.BasePermission
class IsAuthenticatedAndIsOwner(permissions.BasePermission):
    # Override the has_object_permission method to implement custom object-level permission checks
    def has_object_permission(self, request, view, obj):
        # Check if the request user is authenticated (logged in) using request.user.is_authenticated
        # and if the user associated with the object (obj.user) matches the request user (request.user)
        # If both conditions are True, the permission check passes, and the user has permission to perform the requested action on the object.
        return request.user.is_authenticated and obj.user == request.user
