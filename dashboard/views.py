from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    user_data = {
        "calories_eaten": 1200,
        "calorie_goal": 2000,
        "protein": 60,
        "fat": 30,
        "carbs": 80,
        "recipes_api_url": "/recipes/",  # Link to the API endpoint
        "recipes": [
            {"meal": "Breakfast", "image": "path/to/image1.jpg", "calories": 300, "prep_time": "10 min"},
            {"meal": "Lunch", "image": "path/to/image2.jpg", "calories": 400, "prep_time": "15 min"},
            {"meal": "Dinner", "image": "path/to/image3.jpg", "calories": 500, "prep_time": "20 min"},
            {"meal": "Snack", "image": "path/to/image4.jpg", "calories": 100, "prep_time": "5 min"},
        ],
        "water_intake": 1000,  # in ml
        "water_goal": 2000,
    }
    return render(request, 'dashboard/dashboard.html', user_data)