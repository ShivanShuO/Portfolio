# Create your views here.
import os
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from .models import Project,resume

def index(request):
    prj = Project.objects.all()
    allres = resume.objects.all() 
    return render(request,'file/index.html',{'prj':prj, 'ares':allres})

def proj(request):
    prj = Project.objects.all()
    return render(request,'file/project.html',{'prj':prj})

def pro_detail(request, prj_id):
    prj = get_object_or_404(Project, pk=prj_id)
    return render(request,'file/prj-details.html',{'prj':prj})
