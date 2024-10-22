from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Signal handler that ensures a Profile is created or updated whenever a User is saved.

    If the User is being created for the first time, it will attempt to create a related Profile.
    If the User already exists, the Profile will be updated instead.
    
    Args:
        sender (Model): The model class (User) sending the signal.
        instance (User): The instance of the User model being saved.
        created (bool): Boolean indicating whether the User was created (True) or updated (False).
    """
    if created:
        # Only create a profile if one doesn't already exist
        Profile.objects.get_or_create(user=instance)
    else:
        # Update the profile if the user is being saved and the profile already exists
        instance.profile.save()
