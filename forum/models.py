from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from math import ceil


class Section(models.Model):
    """
    Forum sections: they divide the forum into categories.
    Each section has several discussions.
    """
    section_name = models.CharField(max_length=100)
    section_description = models.CharField(max_length=200, blank=True, null=True)
    section_logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.section_name

    def get_absolute_url(self):
        return reverse("show_section", kwargs={'pk': self.pk})

    def get_last_discussions(self):
        return Discussion.objects.filter(discussion_section=self).order_by("-discussion_creation_data")[:3]

    def get_number_posts_in_section(self):
        return Post.objects.filter(post_discussion__discussion_section=self).count()

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'


class Discussion(models.Model):
    """
    Discussion: a topic starting a discussion.
    Every user can start a discussion.
    A discussion lies inside a section.
    """
    discussion_title = models.CharField(max_length=150)
    discussion_creation_data = models.DateField(auto_now_add=True)
    discussion_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')
    discussion_section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.discussion_title

    def get_absolute_url(self):
        return reverse("show_discussion", kwargs={'pk': self.pk})

    def get_number_pages(self):
        discussion_posts = self.post_set.count()
        number_pages = ceil(discussion_posts / 5)
        return number_pages

    class Meta:
        verbose_name = 'Discussion'
        verbose_name_plural = 'Discussions'


class Post(models.Model):
    """
    Post: a message in a discussion.
    Every user can make a post into a discussion.
    """
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post_content = models.TextField()
    post_creation_data = models.DateField(auto_now_add=True)
    post_discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_author.username

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
