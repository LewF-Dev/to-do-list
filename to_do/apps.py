from django.apps import AppConfig


class ToDoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'to_do'

    def ready(self):
        import to_do.signals
