from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthday = models.DateField(null=True)
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    tags = models.BooleanField()

