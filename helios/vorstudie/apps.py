from django.apps import AppConfig


class VorstudieConfig(AppConfig):
    name = 'helios.vorstudie'

    def ready(self):
        import helios.vorstudie.signals