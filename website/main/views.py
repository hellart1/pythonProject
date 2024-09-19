from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        if 'add_task' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('index')

        elif 'delete_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            task.delete()
            return redirect('index')

    return render(request, "main/index.html", {'title': 'Главная страница сайта', 'tasks': tasks, 'form': form})

def test(request):
    return render(request, template_name="main/test.html")