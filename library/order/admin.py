from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'created_at', 'plated_end_at', 'end_at')
    list_filter = ('book', 'user', 'created_at', 'end_at')
    search_fields = ('user__email', 'book__name')

    readonly_fields = ('created_at',)

    fieldsets = (
        ('General Information', {
            'fields': ('user', 'book'),
            'description': 'Details about the user and the borrowed book.'
        }),
        ('Dates and Status', {
            'fields': ('created_at', 'plated_end_at', 'end_at'),
            'description': 'Information regarding the issue date, planned return, and actual return.'
        }),
    )