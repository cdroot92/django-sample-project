from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    name = models.CharField("Name of User", blank=True, max_length=255)
    first_name = None
    last_name = None

    class Meta:
        db_table = "users"

    def longtime_no_see(self):
        if timezone.now() - self.last_login > timedelta(days=30):
            return True
        return False
