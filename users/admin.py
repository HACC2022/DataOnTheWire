from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ['username', 'email', 'department', 'is_admin']


admin.site.register(User, CustomUserAdmin)
