from django.contrib import admin

from .models import Car, Comment


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'description', 'created_at', 'owner')
    search_fields = ('make', 'model', 'year')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'car', 'author')
    search_fields = ('content', 'car__make', 'author__username')
