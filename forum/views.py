from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

from .forms import DiscussionModelForm
from .mixins import StaffMixin
from .models import Discussion, Post, Section


class CreateSection(StaffMixin, CreateView):
    model = Section
    fields = "__all__"
    template_name = "create_section.html"
    success_url = "/"


def show_section(request, pk):
    section = get_object_or_404(Section, pk=pk)
    section_discussions = Discussion.objects.\
        filter(discussion_section=section).order_by("-discussion_creation_data")
    context = {'section': section, 'section_discussions': section_discussions}
    return render(request, "show_section.html", context)


@login_required()
def create_discussion(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == "POST":
        form = DiscussionModelForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.discussion_section = section
            discussion.discussion_author = request.user
            discussion.save()

            first_post = Post.objects.create(
                post_discussion=discussion,
                post_author=request.user,
                post_content=form.cleaned_data['content']
            )

            return HttpResponseRedirect(discussion.get_absolute_url())
    else:
        form = DiscussionModelForm()
    context = {"form": form, "section": section}
    return render(request, "create_discussion.html", context)


def show_discussion(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    discussion_posts = Post.objects.filter(post_discussion=discussion)
    context = {'discussion': discussion, 'discussion_posts': discussion_posts}
    return render(request, "show_discussion.html", context)
