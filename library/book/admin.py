from django.contrib import admin
from .models import Book
from order.models import Order

class OrderInline(admin.StackedInline):
    model = Order
    extra = 1
    readonly_fields = ('created_at',)
    fields = (('user', 'plated_end_at'), 'end_at')
    verbose_name_plural = "Book Orders"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count', 'display_authors')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name', 'authors')
    search_fields = ('name', 'description', 'authors__surname')

    fieldsets = (
        ('Static Data (Unchanged)', {
            'fields': ('name', 'description'), 
            'description': 'Basic information about the publication.'
        }),
        ('Dynamic Data (Changed)', {
            'fields': ('count',), 
        }),
    )

    inlines = [OrderInline]

    def display_authors(self, obj):
        return ", ".join([f"{a.surname} {a.name}" for a in obj.authors.all()])
    
    display_authors.short_description = 'Authors'