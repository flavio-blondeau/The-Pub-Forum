from django.urls import path
from .views import CreateSection, show_section, create_discussion, show_discussion

urlpatterns = [
    path("new-section/", CreateSection.as_view(), name='create_section'),
    path("section/<int:pk>/", show_section, name='show_section'),
    path("section/<int:pk>/new-discussion/", create_discussion, name='create_section'),
    path("/discussion/<int:pk>/", show_discussion, name='show_discussion')
]
