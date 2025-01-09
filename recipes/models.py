from django.db import models
from django.utils.text import slugify

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # Added slug field
    description = models.TextField()
    ingredients = models.TextField()  # Comma-separated list or JSON for detailed data
    steps = models.TextField()       # Step-by-step instructions
    nutritional_info = models.JSONField()  # Store calories, macronutrients, etc.
    preparation_time = models.PositiveIntegerField()  # In minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it doesn't already exist
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

