from django.urls import path

from .resources.profile import Profiles
from .resources import Login

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('profile/', Profiles.as_view(), name='profile'),
]
