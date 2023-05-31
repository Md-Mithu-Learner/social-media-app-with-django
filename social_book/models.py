from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.FileField(upload_to='social_book/profile', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.FileField(upload_to='social_book/post_images')
    caption= models.TextField()
    no_of_likes = models.IntegerField(default=0)
    created_at= models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id=models.CharField(max_length=300)
    username=models.CharField(max_length=200)

    def __str__(self):
        return self.username
class FollowersCount(models.Model):
    follower=models.CharField(max_length=300, blank=True, null=True)
    user=models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.user




