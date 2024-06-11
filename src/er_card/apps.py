from django.apps import AppConfig


class ErCardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.er_card'

    def ready(self):
        import src.er_card.signals