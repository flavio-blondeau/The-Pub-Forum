from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    """
    Forum sections: they divide the forum into categories.
    Each section has several discussions.
    """
    section_name = models.CharField(max_length=100)
    section_desc = models.CharField(max_length=200, blank=True, null=True)
    section_logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'


class Discussion(models.Model):
    """
    Discussion: a topic starting a discussion.
    Every user can start a discussion.
    A discussion lies inside a section.
    """
    disc_title = models.CharField(max_length=150)
    disc_creation_data = models.DateField(auto_now_add=True)
    disc_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')
    disc_section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.disc_title

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
