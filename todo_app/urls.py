from django.urls import path

from todo_app import views


urlpatterns = [
    # Add Task url
    path("add/", views.addTask, name="addTask"),
    
    # Mark As Done url
    path("mark_as_done/<int:pk>/",views.markAsDone, name = "markAsDone"),
    
    # Mark As Undone url
    path("mark_as_undone/<int:pk>/",views.markAsUndone, name = "markAsUndone"),
    
    # Edit Task Url
    path("edit/<int:pk>/", views.editTask, name = "editTask"),
    
    # Delete Task url
    path("delete/<int:pk>/", views.deleteTask, name = "deleteTask"),
]
