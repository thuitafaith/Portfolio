from django.shortcuts import render
from .models import Project,Skill,Personal_Information
# Create your views here.
def home(request):
    title = "FAITH THUITA"
    information = Personal_Information.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    for info in information:
        information = info
    return render(request, 'home.html', {'title': title, 'projects': projects,
                                          'information': information, 'skills': skills})
