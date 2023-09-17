from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ObreplaceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.obreplace_app'
    verbose_name = _('ObreplaceApp')
