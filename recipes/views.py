from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeList(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

class RecipeDetail(APIView):
    def get(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)  # Query by slug instead of pk
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
