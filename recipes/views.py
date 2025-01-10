from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeList(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        diet = request.query_params.get('diet')
        cuisine = request.query_params.get('cuisine')

        recipes = Recipe.objects.all()

        if category:
            recipes = recipes.filter(category=category)
        if diet:
            recipes = recipes.filter(diet=diet)
        if cuisine:
            recipes = recipes.filter(cuisine=cuisine)

        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

class RecipeDetail(APIView):
    def get(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)  # Query by slug instead of pk
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)


