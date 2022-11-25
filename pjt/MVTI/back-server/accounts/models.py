from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Mvti


# Create your models here.
class User(AbstractUser):
    mvti = models.ForeignKey(Mvti, on_delete=models.CASCADE, null=True)