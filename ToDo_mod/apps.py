from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ToDo_mod'

    verbose_name = _("Сделай")  # todo переименовать приложение