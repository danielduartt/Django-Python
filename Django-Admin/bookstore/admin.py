from django.contrib import admin
from .models import Autor, Book

class BookInline(admin.TabularInline):
    model = Book
    extra = 1

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    inlines = [BookInline]

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author__name')

admin.site.register(Autor, AuthorAdmin)
admin.site.register(Book, BookAdmin)

