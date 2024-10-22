from django.apps import AppConfig

class ToDoConfig(AppConfig):
    """
    Configuration class for the 'to_do' app.
    
    This is where app-specific settings are defined, including auto-field configuration 
    and the signal registration upon app readiness.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'to_do'

    def ready(self):
        """
        Method called when the app is ready.

        This ensures that the custom signal handlers in 'signals.py' are registered when the app starts.
        """
        import to_do.signals
