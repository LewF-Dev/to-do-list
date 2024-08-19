from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField  # Assuming you're using Cloudinary for media storage

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='tasks/', blank=True, null=True)
    date = models.DateField(default=datetime.now)
    time = models.TimeField(default=datetime.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True, null=True)  # Temporarily allow null
    profile_picture = CloudinaryField('image', default='default_profile_pic.jpg')
    
    # Add a new field for display name
    display_name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'{self.display_name or self.user.username} Profile'





# Automatically create or update a user's profile when a User object is created/updated
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create profile with display_name defaulting to username
        Profile.objects.create(user=instance, username=instance.username, display_name=instance.username)
    else:
        # Ensure the display name defaults to the username if not provided
        profile = instance.profile
        if not profile.display_name:
            profile.display_name = profile.user.username
        profile.save()
