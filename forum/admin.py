from django.contrib import admin
from .models import Discussion, Post, Section


class DiscussionModelAdmin(admin.ModelAdmin):
    model = Discussion
    list_display = ['discussion_title', 'discussion_section', 'discussion_author']
    search_fields = ['discussion_title', 'discussion_author']
    list_filter = ['discussion_creation_data', 'discussion_section']


class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['post_author', 'post_discussion']
    list_filter = ['post_author', 'post_creation_data']
    search_fields = ['post_content']


class SectionModelAdmin(admin.ModelAdmin):
    model = Section
    list_display = ['section_name', 'section_description']


admin.site.register(Discussion, DiscussionModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Section, SectionModelAdmin)
