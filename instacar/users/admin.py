from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
