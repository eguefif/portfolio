from django.shortcuts import render
from django.template import loader

from .models import Project

def index(request):
    projects = Project.objects.order_by("-date")
    context = {
            "projects": projects,
            }
    return render(request, "pf/index.html", context)
