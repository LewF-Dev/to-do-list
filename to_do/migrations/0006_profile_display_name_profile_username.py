from django.db import migrations, models

# This function will backfill the username and display_name fields for existing Profile instances.
def backfill_usernames_and_display_names(apps, schema_editor):
    Profile = apps.get_model('to_do', 'Profile')
    for profile in Profile.objects.all():
        # Set username to the associated user's username if it's not already set
        if not profile.username:
            profile.username = profile.user.username  
        
        # Set display_name to username if display_name is not already set
        if not profile.display_name:
            profile.display_name = profile.username
        
        profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0005_profile'),  # Ensure this points to the correct previous migration
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='display_name',
            field=models.CharField(blank=True, max_length=150, default='DEFAULT', null=False),  # Set a temporary default value
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        # Add the RunPython operation to backfill both username and display_name
        migrations.RunPython(backfill_usernames_and_display_names),  
        # Now remove the default from display_name and ensure null=False
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(blank=True, max_length=150, null=False),  # Remove default after backfill
        ),
        # Now remove null=True from the username field
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
