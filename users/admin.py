from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ['email', 'department', 'is_active']

    list_filter = ('is_active',)

    fieldsets = (
        (None, {
            'fields': ('department',)
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    readonly_fields = (
        'is_staff', 'is_superuser', 'groups', 'user_permissions', 'department', 'first_name', 'last_name', 'email',
    )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return self.readonly_fields


admin.site.register(User, CustomUserAdmin)
