from django.urls import path
from .views import add_post, CreateSection, DeletePost, show_section, create_discussion, show_discussion

urlpatterns = [
    path("new-section/", CreateSection.as_view(), name='create_section'),
    path("section/<int:pk>/", show_section, name='show_section'),
    path("section/<int:pk>/new-discussion/", create_discussion, name='create_discussion'),
    path("discussion/<int:pk>/", show_discussion, name='show_discussion'),
    path("discussion/<int:pk>/add-post/", add_post, name='add_post'),
    path("discussion/<int:id>/delete-post/<int:pk>/", DeletePost.as_view(), name='delete_post'),
]
