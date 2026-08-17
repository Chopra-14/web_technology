from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
]