from django.db import models
from django.contrib.auth.models import AbstractUser


class ChatUser(AbstractUser):

    username = models.CharField(max_length=100, unique=True)

    email = None

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username