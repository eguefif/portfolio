from django.shortcuts import render
from django.template import loader, Context

from .models import Project, Skill, Technology, ProjectImage

def get_project_dict(db_project, n):
    project = {}
    project["title"] = db_project.title
    project["github"] = db_project.github
    project["description"] = db_project.description
    project["tech"] = Technology.objects.all().filter(project__title__contains=db_project.title)
    project["skill"] = Skill.objects.all().filter(project__title__contains=db_project.title)
    imgs = ProjectImage.objects.all().filter(project__title__contains=db_project.title)
    project["images"] = []
    n = 1
    for i in imgs:
        if i.image:
            project["images"].append({"n": n, "url": i.image.url})
            n += 1
    project["image"] = db_project.image
    project["img_nbr"] = len(project["images"])
    project["n"] = n
    return project


def index(request):
    projects = []

    db_projects = Project.objects.order_by("-date")

    for i, db_project in enumerate(db_projects):
        projects.append(get_project_dict(db_project, i))

    context = {
            "projects": projects,}
    return render(request, "pf/index.html", context)
