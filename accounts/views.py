from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Avatar  # Use Avatar model for profile picture selection

def landing_page(request):
    """
    Renders the landing page with links to login and signup.
    Authenticated users will be redirected to the dashboard.
    """
    if request.user.is_authenticated:  # Redirect authenticated users to the dashboard
        return redirect('dashboard')  # Replace 'dashboard' with the correct URL name for the dashboard
    return render(request, 'accounts/landing.html')

def signup_view(request):
    if request.user.is_authenticated:  # Redirect if user is already logged in
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        avatar_id = request.POST.get('avatar')
        if form.is_valid() and avatar_id:
            user = form.save()  # Create the user
            avatar = Avatar.objects.get(id=avatar_id)
            user.profile.avatar = avatar
            user.profile.save()
            messages.success(request, 'Account created successfully!')
            return redirect('landing')  # Redirect to the landing page after signup
        else:
            if not avatar_id:
                messages.error(request, 'Please select an avatar.')
    else:
        form = UserCreationForm()

    avatars = Avatar.objects.all()
    return render(request, 'accounts/signup.html', {'form': form, 'avatars': avatars})