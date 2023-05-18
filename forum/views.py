from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView

from .forms import DiscussionModelForm, PostModelForm
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
    answer_form = PostModelForm()
    context = {'discussion': discussion,
               'discussion_posts': discussion_posts,
               'answer_form': answer_form
               }
    return render(request, "show_discussion.html", context)


def add_post(request, pk):  # here the pk is the discussion's one
    discussion = get_object_or_404(Discussion, pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.post_discussion = discussion
            form.instance.post_author = request.user
            form.save()
            discussion_url = reverse("show_discussion", kwargs={"pk": pk})
            return HttpResponseRedirect(discussion_url)
    else:
        return HttpResponseBadRequest()
