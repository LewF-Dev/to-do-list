from django import forms
from .models import Task, Profile
from django.utils import timezone
from datetime import datetime

class TaskForm(forms.ModelForm):
    """
    Form for creating or editing a Task object. 
    Includes fields for title, description, date, and time.
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'step': 1})  # Added 'step' attribute for time input
        }

    def clean(self):
        cleaned_data = super().clean()
        task_date = cleaned_data.get("date")
        task_time = cleaned_data.get("time")

        if task_date and task_time:
            # Combine date and time to form a full datetime object
            task_datetime = datetime.combine(task_date, task_time)
            # Make the datetime timezone-aware
            task_datetime = timezone.make_aware(task_datetime, timezone.get_current_timezone())
            current_datetime = timezone.now()

            # Check if the selected date/time is in the past
            if task_datetime < current_datetime:
                raise forms.ValidationError("You cannot set a task for a past date or time. Please choose a future date and time.")

        return cleaned_data


class ProfileForm(forms.ModelForm):
    """
    Form for updating the user's profile.
    Includes fields for profile picture and display name.
    """
    class Meta:
        model = Profile
        fields = ['profile_picture', 'display_name']  # Added display_name to form
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
