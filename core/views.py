from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

from forum.models import Discussion, Post, Section


class Homepage(ListView):
    queryset = Section.objects.all()
    template_name = "homepage.html"


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_discussions = Discussion.objects.filter(discussion_author=user).order_by("-pk")
    context = {'user': user, 'user_discussions': user_discussions}
    return render(request, "user_profile.html", context)


class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = "users.html"


def search(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        if len(querystring) == 0:
            return redirect("/search/")
        discussions = Discussion.objects.filter(discussion_title__icontains=querystring)
        posts = Post.objects.filter(post_content__icontains=querystring)
        users = User.objects.filter(username__icontains=querystring)
        context = {
            'discussions': discussions,
            'posts': posts,
            'users': users
        }
        return render(request, "search.html", context)
    else:
        return render(request, "search.html")

