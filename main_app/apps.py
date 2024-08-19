from django.apps import AppConfig

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils import timezone



class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'

    def ready(self):
        from .models import Reward

        def create_rewards(sender, **kwargs):
            if sender.name == 'main_app':  # Ensure it runs only for your app
                rewards = [
                    {'description': 'Coupon A', 'date': timezone.now()},
                    {'description': 'Coupon B', 'date': timezone.now()},
                    {'description': 'Coupon C', 'date': timezone.now()},
                    {'description': 'Reward 1', 'date': timezone.now()},
                    {'description': 'Reward 2', 'date': timezone.now()},
                ]
                for reward in rewards:
                    Reward.objects.get_or_create(**reward)

        post_migrate.connect(create_rewards, sender=self)

from django.apps import AppConfig

class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'
