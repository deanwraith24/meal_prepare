from django.urls import path, include  # Import include here
from .views import landing_page, signup_view

urlpatterns = [
    path('', landing_page, name='landing'),
    path('signup/', signup_view, name='signup'),
    # Include Django's built-in auth URLs for login
    path('accounts/', include('django.contrib.auth.urls')),
]



