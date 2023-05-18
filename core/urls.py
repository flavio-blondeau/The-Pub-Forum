from django.urls import path
from .views import homepage, user_profile, UserList

urlpatterns = [
    path('', homepage, name="homepage"),
    path('user/<str:username>/', user_profile, name="user_profile"),
    path('users/', UserList.as_view(), name='user_list')
]
