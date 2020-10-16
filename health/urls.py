from django.urls import path

from .resources import Health

urlpatterns = [
    path('', Health.as_view()),
]