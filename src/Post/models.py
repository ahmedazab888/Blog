from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Post => user, title, image, content, date


class Post(models.Model):
    user = models.ForeignKey(User, on_delete='None')
    title = models.CharField(max_length=255)
    content = models.TextField(default='')
    img = models.ImageField(upload_to='post_img/',
                            default='post_img/default.png')
    created_date = models.DateTimeField(default=timezone.now)



