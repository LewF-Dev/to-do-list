from django import forms
from .models import Task, Profile

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
