# signals.py

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile,Product,Ilac
from django.core.cache import cache


User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a profile with the user, leaving the photo field empty
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Product)
@receiver(post_save, sender=Ilac)
@receiver(post_delete, sender=Product)
@receiver(post_delete, sender=Ilac)
def clear_cache(sender, **kwargs):
    # Önbellekten verileri kontrol ediyoruz
    combined_data = cache.get('combined_data')

    if combined_data is not None:
        # Önbellekten verileri temizliyoruz
        cache.delete('combined_data')
