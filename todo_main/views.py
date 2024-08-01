from django.http import HttpResponse
from django.shortcuts import render

from todo_app.models import Task


def home(request):
    all_tasks = Task.objects.filter(is_completed = False).order_by("-updated_at")
    completed_tasks = Task.objects.filter(is_completed = True)
    # print(all_tasks)
    # print(completed_tasks)
    context = {
        "all_tasks" : all_tasks,
        "completed_tasks" : completed_tasks
    }
    return render(request, "home.html", context)

# def get_all_tasks(request):
#     all_tasks = Task.objects.all()
#     print(all_tasks)