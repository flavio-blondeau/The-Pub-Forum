from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from forum.models import Section


class Homepage(ListView):
    queryset = Section.objects.all()
    template_name = "homepage.html"


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user': user}
    return render(request, "user_profile.html", context)


class UserList(ListView):
    model = User
    template_name = "users.html"
