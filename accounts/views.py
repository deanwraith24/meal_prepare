from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Avatar  # Use Avatar model for profile picture selection


def landing_page(request):
    """
    Renders the landing page with links to login and signup.
    Redirects authenticated users to the dashboard.
    """
    if request.user.is_authenticated:  # Redirect authenticated users to the dashboard
        return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL name

    return render(request, 'accounts/landing.html', {
        'login_url': reverse('login'),  # Dynamically resolve login URL
        'signup_url': reverse('signup'),  # Dynamically resolve signup URL
    })


def signup_view(request):
    """
    Handles user signup, including avatar selection.
    """
    if request.user.is_authenticated:  # Redirect if user is already logged in
        return redirect('dashboard')  # Replace 'dashboard' with your desired URL name

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        avatar_id = request.POST.get('avatar')  # Get selected avatar ID from form
        if form.is_valid() and avatar_id:
            user = form.save()  # Create the user
            try:
                # Fetch the selected avatar and assign it to the user profile
                avatar = Avatar.objects.get(id=avatar_id)
                user.profile.avatar = avatar.url  # Assign the avatar URL to the profile
                user.profile.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')  # Redirect to login page after successful signup
            except Avatar.DoesNotExist:
                messages.error(request, 'Selected avatar does not exist.')
        else:
            if not avatar_id:
                messages.error(request, 'Please select an avatar.')
    else:
        form = UserCreationForm()

    avatars = Avatar.objects.all()  # Fetch all available avatars
    return render(request, 'accounts/signup.html', {'form': form, 'avatars': avatars})



