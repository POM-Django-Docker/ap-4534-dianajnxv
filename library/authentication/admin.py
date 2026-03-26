from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')    
    search_fields = ('email', 'first_name', 'last_name')
    
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'middle_name', 'last_name', 'email', 'password')
        }),
        ('Permissions & Roles', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )