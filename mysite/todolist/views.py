from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    context = {'tasks': tasks}  # Create a dictionary to pass to the template
    return render(request, 'todolist/task_list.html', context)  # Render the template
