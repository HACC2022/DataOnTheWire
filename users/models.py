from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    department = models.CharField(max_length=3)

    class Meta:
        db_table = 'auth_user'
        permissions = (('is_admin', 'Is Deparment Admin'),)
