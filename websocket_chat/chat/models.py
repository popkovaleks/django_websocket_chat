from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    name = models.CharField()

    email = None

    USERNAME_FIELD = name

    def __str__(self):
        return self.name