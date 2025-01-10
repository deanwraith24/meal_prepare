from django.db import models
from django.utils.text import slugify

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    DIET_CHOICES = [
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('gluten_free', 'Gluten-Free'),
        ('keto', 'Keto'),
        ('paleo', 'Paleo'),
        ('none', 'None'),
    ]

    CUISINE_CHOICES = [
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('indian', 'Indian'),
        ('chinese', 'Chinese'),
        ('american', 'American'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # Added slug field
    description = models.TextField()
    ingredients = models.TextField()  # Comma-separated list or JSON for detailed data
    steps = models.TextField()       # Step-by-step instructions
    nutritional_info = models.JSONField()  # Store calories, macronutrients, etc.
    preparation_time = models.PositiveIntegerField()  # In minutes
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='lunch')
    diet = models.CharField(max_length=50, choices=DIET_CHOICES, default='none')
    cuisine = models.CharField(max_length=50, choices=CUISINE_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it doesn't already exist
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



