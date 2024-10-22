from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages  # Import for notifications
from .models import Task, Profile
from .forms import TaskForm, ProfileForm
from django.utils import timezone
from .fetch_holidays import fetch_holidays
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import date

@login_required
def index(request):
    """
    View for displaying the home page with tasks and calendar events.
    """
    tasks = Task.objects.filter(user=request.user, completed=False)
    today = timezone.now().date()
    todays_tasks = tasks.filter(date=today)

    selected_date = request.GET.get('date')
    if selected_date:
        tasks = tasks.filter(date=selected_date)
    else:
        selected_date = today.strftime('%Y-%m-%d')

    # Prepare task events for calendar display
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

    # Fetch holiday data from external API
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

    current_date = today.strftime('%d / %m / %Y')
    important_task = "Most important task description"

    # Retrieve the profile picture URL
    profile = Profile.objects.get(user=request.user)
    profile_picture_url = profile.profile_picture.url if profile.profile_picture else None

    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'todays_tasks': todays_tasks,
        'events_json': events_json,
        'current_date': current_date,
        'important_task': important_task,
        'selected_date': selected_date,
        'profile_picture_url': profile_picture_url,
    })


@login_required
def complete_task(request, task_id):
    """
    Mark a task as completed for the current user and redirect to the home page.
    A success message is displayed upon completion.
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    messages.success(request, f'Task "{task.title}" marked as completed!')
    return redirect('index')


@login_required
def completed_tasks(request):
    """
    View for displaying all completed tasks of the logged-in user.
    """
    tasks = Task.objects.filter(user=request.user, completed=True)
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})


@login_required
def add_task(request):
    """
    Add a new task for the logged-in user. If the form is valid, 
    the task is saved and the user is redirected to the home page.
    """
    initial_date = request.GET.get('date')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('index')
        else:
            if form.non_field_errors():  # Only show specific validation error
                messages.error(request, form.non_field_errors())
            else:
                messages.error(request, 'There was an error creating the task.')
    else:
        form = TaskForm(initial={'date': initial_date})
    return render(request, 'tasks/add_task.html', {'form': form})


@login_required
def edit_task(request, task_id):
    """
    Edit an existing task for the logged-in user. If the form is valid,
    the task is updated and the user is redirected to the home page.
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('index')
        else:
            if form.non_field_errors():  # Only show specific validation error
                messages.error(request, form.non_field_errors())
            else:
                messages.error(request, 'There was an error updating the task.')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})


@login_required
def delete_task(request, task_id):
    """
    Delete a task for the logged-in user. If the delete confirmation is submitted,
    the task is deleted, and the user is redirected to the home page with a success message.
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, f'Task "{task.title}" deleted successfully!')
        return redirect('index')
    return render(request, 'tasks/confirm_delete.html', {'task': task})


@login_required
def profile(request):
    """
    View and update the logged-in user's profile. If the form is valid,
    the profile is updated and the user is redirected to the home page.
    """
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('index')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})


def signup(request):
    """
    Register a new user. If the form is valid, a new user account is created
    and the user is redirected to the login page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
