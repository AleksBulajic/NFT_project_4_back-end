from django.contrib import admin
from .models import UserProfile, Identity

admin.site.register(UserProfile)
admin.site.register(Identity)
