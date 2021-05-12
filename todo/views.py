from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }


    return render(request, 'todo/task_list.html', context)


@login_required(login_url='login')
def task_detail(request, pk):
    task = Task.objects.get(id=pk)

    context = {
        'task': task
    }

    return render(request, 'todo/task_detail.html', context)


@login_required(login_url='login')
def task_create(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks')

    context = {
        'form': form
    }

    return render(request, 'todo/task_create.html', context)


@login_required(login_url='login')
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks')

    context = {
        'form': form
    }

    return render(request, 'todo/task_update.html', context)


@login_required(login_url='login')
def task_delete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('tasks')

    context = {
        'task': task
    }

    return render(request, 'todo/delete_task.html', context)
