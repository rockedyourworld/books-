from django.contrib import admin

from books.models import BookModel, CommentModel

admin.site.register(BookModel)
admin.site.register(CommentModel)
