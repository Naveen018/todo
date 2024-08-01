from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from todo_app.models import Task

# Create your views here.

def addTask(request):
    print(request.POST)
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect("home")

def markAsDone(request, pk):
    task = get_object_or_404(Task, id=pk)
    print(task)
    print(task.created_at)
    print(task.is_completed)
    task.is_completed = True
    task.save()
    return redirect("home")

def markAsUndone(request, pk):
    task = get_object_or_404(Task, id=pk)
    print(task)
    print(task.created_at)
    print(task.is_completed)
    task.is_completed = False
    task.save()
    return redirect("home")

def editTask(request, pk):
    get_task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        print(request.POST)
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect("home")
    else:   
        context = {
            "get_task" : get_task
        }
        return render(request, "edit_task.html", context)
    
def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('home')
    
