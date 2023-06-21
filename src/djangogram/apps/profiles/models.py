from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.username}_profile_pic.{ext}"
    return f'{instance.username}/{filename}'


class DgUser(AbstractUser):
    profile_pic = models.ImageField(upload_to=user_directory_path,
                                    null=True, blank=True)
    bio_info = models.TextField(max_length=1000)


class Follow(models.Model):
    follower = models.ForeignKey(DgUser, on_delete=models.CASCADE, null=True,
                                 related_name='follower')
    following = models.ForeignKey(DgUser, on_delete=models.CASCADE, null=True,
                                  related_name='following')
