from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        "courses": Course.objects.all()
        }
    return render(request, 'index.html', context)

def new_course(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        course = Course.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )
        # desc = Description.objects.create(content=request.POST['desc'])
        # course.description = desc
        course.save()

    return redirect("/")



