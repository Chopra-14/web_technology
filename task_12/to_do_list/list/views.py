from django.shortcuts import render, redirect
from .models import Task


def todo_list(request):

    # ADD / UPDATE
    if request.method == "POST":

        title = request.POST.get("title")
        task_id = request.POST.get("task_id")

        # UPDATE
        if task_id:

            task = Task.objects.get(id=task_id)

            task.title = title

            task.save()

        # ADD
        else:

            Task.objects.create(
                title=title
            )

        return redirect("todo_list")


    # EDIT

    edit_id = request.GET.get("edit")

    edit_task = None

    if edit_id:

        edit_task = Task.objects.get(
            id=edit_id
        )


    # GET ALL TASKS

    tasks = Task.objects.all()


    return render(
        request,
        "todo.html",
        {
            "tasks": tasks,
            "edit_task": edit_task
        }
    )


# DELETE

def delete_task(request, task_id):

    task = Task.objects.get(id=task_id)

    task.delete()

    return redirect("todo_list")