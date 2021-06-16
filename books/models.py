from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class BookModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.CharField(max_length=255)
    is_booked = models.ForeignKey(UserModel, null=True, blank=True, on_delete=models.CASCADE)


class CommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user Comment+')
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='book Comment+')
    text = models.TextField()
