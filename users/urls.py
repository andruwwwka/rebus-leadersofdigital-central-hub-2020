from django.urls import path

from .resources import Login, Profiles

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('profile/', Profiles.as_view(), name='profile'),
]
