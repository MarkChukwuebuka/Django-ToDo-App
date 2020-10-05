from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils import timezone

# Create your views here.
def listTask(request):
    queryset = Task.objects.order_by('complete', 'due')
    form = TaskForm()
    current = timezone.now
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks' : queryset,
        'form' : form,
        'current' : current
    }
    return render(request, 'list_task.html', context)


def updateTask(request, pk):
    queryset = Task.objects.get(id=pk)
    form = UpdateForm(instance = queryset)
    if request.method =='POST':
        form = UpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form
    }
    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    queryset = Task.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/')
    context = {
        'item' : queryset
    }

    return render(request, 'delete_task.html', context)