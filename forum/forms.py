from django import forms
from .models import Discussion


class DiscussionModelForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Write here the content"}),
        max_length=4000
    )

    class Meta:
        model = Discussion
        fields = ['discussion_title', 'content']
        widget = {
            "discussion_title": forms.TextInput(attrs={"placeholder": "Write here the title"})
        }
