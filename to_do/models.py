from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  # Add this line

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='tasks/', blank=True, null=True)
    date = models.DateField(default=datetime.now)  # This line is already correct

    def __str__(self):
        return self.title
