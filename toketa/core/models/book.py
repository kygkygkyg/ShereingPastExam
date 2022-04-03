from django.db import models
from core.models.user import User


class Book(models.Model):
    title = models.CharField(max_length=200, unique=False)
    date_of_issue = models.DateTimeField()
    auther = models.CharField(max_length=200, unique=False)
    created_at = models.DateTimeField(help_text='created time (this data)')