from django.shortcuts import render,redirect
from .models import Project,Skill,Personal_Information
from .email import send_welcome_email
from django.contrib import messages

# Create your views here.
def home(request):
    title = "FAITH THUITA"
    information = Personal_Information.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    # for info in information:
    #     information = info
    return render(request, 'home.html', {'title': title, 'projects': projects,
                                          'information': information, 'skills': skills})
def contact(request):
    if request.method == 'POST' and 'message' in request.POST:
        email_content = request.POST['message']
        name = request.POST['Your Name']
        email = request.POST['Your Email']
        subject = "NAME: "+name + " " + "EMAIL: " + email
        send_welcome_email(subject, email_content)
        messages.success(request, 'Email successfully sent')
    return redirect(home)
