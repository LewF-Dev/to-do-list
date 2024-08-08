from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Task
from .forms import TaskForm

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'

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