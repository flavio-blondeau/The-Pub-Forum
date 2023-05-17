from django.urls import path
from .views import registration_view

urlpatterns = [
    path("registration/", registration_view, name='registration')
]