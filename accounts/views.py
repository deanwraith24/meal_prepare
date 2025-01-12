from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Avatar

def landing_page(request):
    """
    Renders the landing page with links to login and signup.
    Authenticated users will be redirected to the dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect authenticated users to the dashboard
    return render(request, 'accounts/landing.html')

def signup_view(request):
    """
    Handles user registration and avatar selection.
    Uses Django Allauth for the user registration process.
    """
    if request.user.is_authenticated:  # Redirect logged-in users to the dashboard
        return redirect('dashboard')

    avatars = Avatar.objects.all()  # Fetch all available avatars for selection

    return render(request, 'account/signup.html', {'avatars': avatars})