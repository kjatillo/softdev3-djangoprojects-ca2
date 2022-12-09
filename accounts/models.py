from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    fav_book = models.CharField(max_length=255)
    fav_author = models.CharField(max_length=255)
    fav_genre = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    try:
       if created:
          Profile.objects.get_or_create(user=instance)[0]
    except Exception as err:
       print(f'Error creating user profile!\n{err}')
