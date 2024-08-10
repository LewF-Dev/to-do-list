from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'image', 'date']  # Include 'date' field
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  # This will use a date picker in HTML5
        }
