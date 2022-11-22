from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver

from dataonthewire import settings


class User(AbstractUser):
    department = models.CharField(max_length=3)

    class Meta:
        db_table = 'auth_user'
        permissions = (('is_admin', 'Is Deparment Admin'),)


@receiver(pre_save, sender=User, dispatch_uid='active')
def active(sender, instance, **kwargs):
    if instance.is_active and User.objects.filter(pk=instance.pk, is_active=False).exists():
        subject = 'Active account'
        message = '%s your account is now active' % instance.username
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [instance.email], fail_silently=False)