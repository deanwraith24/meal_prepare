from django.urls import path
from .views import landing_page, signup_view

urlpatterns = [
    path('', landing_page, name='landing'),  # Landing page
    path('signup/', signup_view, name='signup'),
]