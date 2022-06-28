from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "model_hub.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import model_hub.users.signals  # noqa F401
        except ImportError:
            pass
