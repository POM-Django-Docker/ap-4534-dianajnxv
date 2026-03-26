from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'patronymic')
    list_display_links = ('id', 'surname')
    list_filter = ('id', 'surname')
    search_fields = ('name', 'surname', 'id')

    filter_horizontal = ('books',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('surname', 'name', 'patronymic'),
            'description': 'Author identity data.'
        }),
        ('Works', {
            'fields': ('books',),
            'description': 'Select books associated with this author.'
        }),
    )