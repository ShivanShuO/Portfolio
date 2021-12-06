from django import forms
from django.forms import fields
from django.forms.fields import FileField
from .models import Project, project, resume

class prjForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'detail', 'logo']

class resForm(forms.ModelForm):
    class Meta:
        model = resume
        fields = ['Resume']