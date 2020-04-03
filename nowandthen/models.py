from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Picture(models.Model):
    TITLE_MAX_LENGTH = 190
    DESCRIPTION_MAX_LENGTH = 1000
    TAG_MAX_LENGTH = 50
    ERA_MAX_LENGTH = 20
    image = models.ImageField(upload_to='shared_pics', unique=True)
    title = models.CharField(max_length=TITLE_MAX_LENGTH, blank=True)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH, blank=True)
    tag_one = models.CharField(max_length=TAG_MAX_LENGTH, blank=True)
    tag_two = models.CharField(max_length=TAG_MAX_LENGTH, blank=True)
    era = models.CharField(max_length=ERA_MAX_LENGTH, blank=True)
    when_added = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['when_added']
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return self.title


# user profile model

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


# Comment model. The comment functionality has not been completed.
class Comment(models.Model):
    COMMENT_MAX_LENGTH = 1000
    image = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    body = models.TextField(max_length=COMMENT_MAX_LENGTH)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)
