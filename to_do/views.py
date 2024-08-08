from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from .models import Task
from .forms import TaskForm
from datetime import datetime

class HomePage(TemplateView):
    template_name = 'index.html'

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    current_date = datetime.now().strftime('%d / %m / %Y')
    important_task = "Most important task description"  # You should replace this with actual logic
    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'current_date': current_date,
        'important_task': important_task
    })

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
