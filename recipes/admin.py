from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'preparation_time', 'created_at')
    search_fields = ('title', 'description')
