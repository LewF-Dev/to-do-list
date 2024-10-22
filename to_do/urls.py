from django.urls import path
from . import views

# Define URL patterns for the task management application.
# Each URL is mapped to a corresponding view function.

urlpatterns = [
    # Home page - displays tasks and calendar view
    path('', views.index, name='index'),
    
    # Add a new task
    path('add/', views.add_task, name='add_task'),
    
    # Edit an existing task by ID
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    
    # Delete an existing task by ID
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    
    # Mark a task as complete by ID
    path('task/<int:task_id>/complete/', views.complete_task, name='complete_task'),
    
    # View all completed tasks
    path('completed-tasks/', views.completed_tasks, name='completed_tasks'),
    
    # User signup page
    path('signup/', views.signup, name='signup'),
    
    # Profile management page
    path('profile/', views.profile, name='profile'),  # New profile URL
]
