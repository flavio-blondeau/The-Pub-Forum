from django.urls import path
from .views import Homepage, search, user_profile, UserList

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('user/<str:username>/', user_profile, name="user_profile"),
    path('users/', UserList.as_view(), name='user_list'),
    path('search/', search, name='search')
]
