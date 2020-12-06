from django.conf import settings

from .django import get_settings_path, get_urlconf_path, load_addon
from .patcher import setup_django, update_setting, update_urlconf


def enable(application: str, verbose: bool = False):
    """
    Enable django application in the current project

    :param str application: python module name to enable. It must be the name of a Django application.
    :param bool verbose: Verbose output
    """
    setup_django()

    setting_file = get_settings_path(settings)
    urlconf_file = get_urlconf_path(settings)
    application_config = load_addon(application)
    if application_config:
        update_setting(setting_file, application_config)
        update_urlconf(urlconf_file, application_config)