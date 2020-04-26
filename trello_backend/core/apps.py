from django.apps import AppConfig


class BoardConfig(AppConfig):
    name = 'core'

    def ready(self):
        import core.signals
