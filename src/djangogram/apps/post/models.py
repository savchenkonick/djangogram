import uuid
from django.db import models

from apps.profiles.models import DgUser


def user_dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_posted = models.ForeignKey(DgUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_dir_path, null=True, blank=True)
    # image = models.ImageField(upload_to='posts/images/',
    #                           null=True, blank=True)
    caption = models.TextField(max_length=1500, verbose_name='Caption')
    time_posted = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)


class Likes(models.Model):
    user = models.ForeignKey(DgUser, on_delete=models.CASCADE,
                             related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='post_like')
