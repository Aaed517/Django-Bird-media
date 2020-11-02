from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class SubComment(models.Model):
    User = models.ForeignKey(User, related_name='user_subcomment',on_delete=models.CASCADE)
    subcomment = models.CharField(max_length=600)
    picture = models.ImageField(upload_to='subcomment_picture', blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=600)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    parent  = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    likes = models.ManyToManyField(User, related_name='comment_user', blank= True, null=True)
    picture = models.ImageField(upload_to='comment_picture', blank=True,null=True)
    subcomments = models.ManyToManyField(SubComment, related_name='sub_comment', blank=True)
