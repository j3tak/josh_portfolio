
from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.filter(is_active=True)

    return render(request, "core/home.html", {
        "projects": projects,
    })
