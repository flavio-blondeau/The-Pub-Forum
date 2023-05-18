from django import forms
from .models import Discussion, Post


class DiscussionModelForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Write here the content"}),
        max_length=4000
    )

    class Meta:
        model = Discussion
        fields = ['discussion_title', 'content']
        widgets = {
            "discussion_title": forms.TextInput(attrs={"placeholder": "Write here the title"})
        }


class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_content']
        widgets = {
            'post_content': forms.Textarea(attrs={'rows': '5'})
        }
        labels = {
            'post_content': 'Add a Post'
        }
