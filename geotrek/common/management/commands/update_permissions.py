import logging

from django.conf import settings
from django.utils.importlib import import_module
from django.db.models import get_apps
from django.contrib.auth.management import create_permissions
from django.core.management.base import BaseCommand

from mapentity import registry
from mapentity.registry import create_mapentity_model_permissions


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create models permissions"

    def execute(self, *args, **options):
        logger.info("Synchronize django permissions")

        for app in get_apps():
            create_permissions(app, [], int(options.get('verbosity', 1)))

        logger.info("Done.")

        logger.info("Synchronize mapentity permissions")

        # Make sure apps are registered at this point
        import_module(settings.ROOT_URLCONF)

        # For all models registered, add missing bits
        for model in registry.registry.keys():
            create_mapentity_model_permissions(model)

        logger.info("Done.")
