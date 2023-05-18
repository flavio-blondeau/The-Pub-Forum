from django.urls import path
from .views import CreateSection, show_section

urlpatterns = [
    path("new-section/", CreateSection.as_view(), name='create_section'),
    path("section/<int:pk>/", show_section, name='show_section')
]
