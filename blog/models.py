from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#post database model

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to='post_thumbnails',blank=True)
    attachment = models.FileField(upload_to='attachment', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #delete post when user get deleted
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk}) #redirect to the created post

