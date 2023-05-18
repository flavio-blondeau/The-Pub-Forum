from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Section
from .mixins import StaffMixin


class CreateSection(StaffMixin, CreateView):
    model = Section
    fields = "__all__"
    template_name = "create_section.html"
    success_url = "/"


def show_section(request, pk):
    section = get_object_or_404(Section, pk=pk)
    context = {'section': section}
    return render(request, "show_section.html", context)
