from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {'placeholder' : 'Enter Task ...'}), label = False)
    due = forms.CharField(widget = forms.TextInput(attrs = {'placeholder' : 'Due date ...'}), label = False)

    class Meta:
        model = Task
        fields = ['title', 'due']


class UpdateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs = {'placeholder' : 'Enter Task ...'}) )

    class Meta:
        model = Task
        fields = ['title', 'due', 'complete']