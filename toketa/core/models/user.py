from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email' # usernameのuniqueをTrueにしない場合、どれか一つのカラムをTrueにする必要がある。
    REQUIRED_FIELDS = ['username']
