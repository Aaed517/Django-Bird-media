from django.contrib import admin

from .models import Comment, CommentLike, SubComment
# Register your models here.
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(SubComment)