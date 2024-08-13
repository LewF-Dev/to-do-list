import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Task
from .forms import TaskForm
from datetime import datetime
from .fetch_holidays import fetch_holidays  # Import the fetch_holidays function

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user, completed=False)  # Filter out completed tasks
    selected_date = request.GET.get('date')
    if selected_date:
        tasks = tasks.filter(date=selected_date)  # Filter tasks by the selected date
    else:
        selected_date = datetime.now().strftime('%Y-%m-%d')  # Default to current date

    # Convert tasks to a JSON format for FullCalendar
    events = [
        {
            "title": task.title,
            "start": task.date.strftime('%Y-%m-%d'),  # format the date to 'YYYY-MM-DD'
            "description": task.description,  # Add description here
            "editUrl": reverse('edit_task', args=[task.id]),  # Add edit URL
            "deleteUrl": reverse('delete_task', args=[task.id])  # Add delete URL
        }
        for task in tasks
    ]

    # Fetch holidays using the fetch_holidays function
    api_key = "8XGSItroiyWeOXGrvak1jgPrJflsnpxr"  # Replace with your actual Calendarific API key
    country_code = "GB"  # Replace with the appropriate country code
    holidays = fetch_holidays(api_key, country_code)

    # Print the holidays to ensure they're being fetched correctly
    print(f"Holidays fetched: {holidays}")

    if holidays:
        # Convert holidays to the same event format and add isHoliday flag
        holiday_events = [
            {
                "title": holiday['name'],
                "start": holiday['date']['iso'],  # Use the ISO date format
                "description": holiday.get('description', 'Holiday'),  # Use description if available
                "backgroundColor": "#ff9f89",  # Example color for holiday events
                "borderColor": "#ff9f89",  # Example border color for holiday events
                "textColor": "#000000",  # Example text color for holiday events
                "isHoliday": True  # Mark this event as a holiday
            }
            for holiday in holidays
        ]
        events.extend(holiday_events)  # Add holiday events to the existing events list

    # Print the final events list to debug
    print(f"Final events: {events}")

    events_json = json.dumps(events, cls=DjangoJSONEncoder)

    current_date = datetime.now().strftime('%d / %m / %Y')
    important_task = "Most important task description"  # Replace this with actual logic
    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'events_json': events_json,
        'current_date': current_date,
        'important_task': important_task,
        'selected_date': selected_date,  # Pass the selected date to the template
    })


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('index')

@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, completed=True)  # Get only completed tasks
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})

@login_required
def add_task(request):
    initial_date = request.GET.get('date')  # Get the date from the query parameter if available
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm(initial={'date': initial_date})  # Pre-fill the date field if available
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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
