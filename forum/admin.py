from django.contrib import admin
from .models import Discussion, Post, Section


class DiscussionModelAdmin(admin.ModelAdmin):
    model = Discussion
    list_display = ['disc_title', 'disc_section', 'disc_author']
    search_fields = ['disc_title', 'disc_author']
    list_filter = ['disc_creation_data', 'disc_section']


class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['post_author', 'post_discussion']
    list_filter = ['post_author', 'post_creation_data']
    search_fields = ['post_content']


class SectionModelAdmin(admin.ModelAdmin):
    model = Section
    list_display = ['section_name', 'section_desc']


admin.site.register(Discussion, DiscussionModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Section, SectionModelAdmin)
