from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    Handles user registration. Users must select an avatar and complete the registration form.
    """
    if request.user.is_authenticated:  # Redirect logged-in users to the dashboard
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        avatar_id = request.POST.get('avatar')

        if form.is_valid() and avatar_id:
            user = form.save()  # Create the user
            avatar = get_object_or_404(Avatar, id=avatar_id)  # Ensure valid avatar ID
            user.profile.avatar = avatar  # Associate the selected avatar with the user's profile
            user.profile.save()

            # Log in the user after successful signup (optional)
            from django.contrib.auth import login
            login(request, user)

            messages.success(request, 'Your account has been created successfully!')
            return redirect('dashboard')  # Redirect to the dashboard after signup

        # Handle form and avatar selection errors
        if not avatar_id:
            messages.error(request, 'Please select an avatar.')
        elif not form.is_valid():
            messages.error(request, 'Please correct the errors in the form.')

    else:
        form = UserCreationForm()

    avatars = Avatar.objects.all()  # Fetch all available avatars for selection
    return render(request, 'accounts/signup.html', {'form': form, 'avatars': avatars})
