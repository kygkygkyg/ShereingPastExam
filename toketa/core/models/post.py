from django.db import models
from core.models.user import User
from core.models.book import Book


class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
    post_info = models.CharField(max_length=300, unique=False)
    path_docs = models.CharField(max_length=300, unique=True)
    created_at =  models.DateTimeField(help_text='created time (this data)')
