from django.shortcuts import render
from django.template import loader, Context

from .models import Project, Skill, Technology

def index(request):
    projects = Project.objects.order_by("-date")
    context = {
            "projects": projects,
            }

    return render(request, "pf/index.html", context)

def project(request, pk):
    project = Project.objects.get(pk=pk)
    skills = Skill.objects.all().filter(
            project__title__contains=project.title)
    technologies = Technology.objects.all().filter(
            project__title__contains=project.title)
    context = {
            "project": project,
            "skills": skills,
            "technologies": technologies,
            }
    return render(request, "pf/project.html", context)
