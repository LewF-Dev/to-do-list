from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'image', 'date', 'time']  # Include 'date' and 'time' fields
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # This will use a date picker in HTML5
            'time': forms.TimeInput(attrs={'type': 'time'})   # This will use a time picker in HTML5
        }
