from django.urls import path
from .views import RecipeList, RecipeDetail
from django.views.generic import TemplateView  # For a basic template view

urlpatterns = [
    path('', RecipeList.as_view(), name='recipe-list'),
    path('<slug:slug>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('list/', TemplateView.as_view(template_name='recipes/recipes_list.html'), name='recipes_list'),
]


