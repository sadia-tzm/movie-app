from django.apps import AppConfig


class MovieappConfig(AppConfig):
    '''This class defines and configures the app.'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movieapp'