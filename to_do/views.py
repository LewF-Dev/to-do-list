from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Task, Profile
from .forms import TaskForm, ProfileForm
from datetime import datetime
from .fetch_holidays import fetch_holidays
import json
from django.core.serializers.json import DjangoJSONEncoder


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user, completed=False)
    selected_date = request.GET.get('date')
    if selected_date:
        tasks = tasks.filter(date=selected_date)
    else:
        selected_date = datetime.now().strftime('%Y-%m-%d')

    events = [
        {
            "title": task.title,
            "start": task.date.strftime('%Y-%m-%d'),
            "description": task.description,
            "editUrl": reverse('edit_task', args=[task.id]),
            "deleteUrl": reverse('delete_task', args=[task.id])
        }
        for task in tasks
    ]

    api_key = "8XGSItroiyWeOXGrvak1jgPrJflsnpxr"
    country_code = "GB"
    holidays = fetch_holidays(api_key, country_code)

    if holidays:
        holiday_events = [
            {
                "title": holiday['name'],
                "start": holiday['date']['iso'],
                "description": holiday.get('description', 'Holiday'),
                "backgroundColor": "#ff9f89",
                "borderColor": "#ff9f89",
                "textColor": "#000000",
                "isHoliday": True
            }
            for holiday in holidays
        ]
        events.extend(holiday_events)

    events_json = json.dumps(events, cls=DjangoJSONEncoder)

    current_date = datetime.now().strftime('%d / %m / %Y')
    important_task = "Most important task description"

    # Pass the profile picture URL to the template
    profile = Profile.objects.get(user=request.user)
    profile_picture_url = profile.profile_picture.url if profile.profile_picture else None

    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'events_json': events_json,
        'current_date': current_date,
        'important_task': important_task,
        'selected_date': selected_date,
        'profile_picture_url': profile_picture_url,  # Add this line
    })

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('index')

@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, completed=True)
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})

@login_required
def add_task(request):
    initial_date = request.GET.get('date')
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm(initial={'date': initial_date})
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'tasks/confirm_delete.html', {'task': task})

@login_required
def profile(request):
    # Ensure the profile exists for the user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
