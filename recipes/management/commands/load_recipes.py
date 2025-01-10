from django.core.management.base import BaseCommand
from recipes.models import Recipe
from django.utils.text import slugify  # Import slugify for generating slugs

class Command(BaseCommand):
    help = "Load sample recipes into the database"

    def handle(self, *args, **kwargs):
        recipes = [
            {
                "title": "Vegan Buddha Bowl",
                "slug": slugify("Vegan Buddha Bowl"),  # Explicitly define slug
                "description": "A nourishing bowl packed with plant-based goodness.",
                "ingredients": "Quinoa, Chickpeas, Spinach, Tahini, Lemon Juice",
                "steps": "1. Cook quinoa. 2. Prepare chickpeas. 3. Assemble bowl.",
                "nutritional_info": {"calories": 450, "protein": 20, "carbs": 50, "fat": 15},
                "preparation_time": 30,
                "category": "lunch",
                "diet": "vegan",
                "cuisine": "other",
            },
            {
                "title": "Grilled Chicken Salad",
                "slug": slugify("Grilled Chicken Salad"),  # Explicitly define slug
                "description": "A light and protein-packed chicken salad.",
                "ingredients": "Chicken Breast, Romaine Lettuce, Cherry Tomatoes, Olive Oil, Lemon Juice",
                "steps": "1. Grill chicken. 2. Chop vegetables. 3. Toss salad.",
                "nutritional_info": {"calories": 350, "protein": 40, "carbs": 10, "fat": 10},
                "preparation_time": 25,
                "category": "dinner",
                "diet": "none",
                "cuisine": "american",
            },
            # Add more recipes as needed
        ]

        for recipe_data in recipes:
            Recipe.objects.create(**recipe_data)
        
        self.stdout.write(self.style.SUCCESS("Recipes loaded successfully!"))


