from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    
    if created:
        print('create profile.')
        Profile.objects.create(user=instance)
        save_profile(instance)


def save_profile(instance):
    print('save profile.')
    instance.profile.save()