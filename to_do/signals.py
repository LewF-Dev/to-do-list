from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Only create a profile if one doesn't already exist
        Profile.objects.get_or_create(user=instance)
    else:
        # Update the profile if the user is being saved and the profile already exists
        instance.profile.save()
