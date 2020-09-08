from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from phone_field import PhoneField
from localflavor.us.models import USStateField,USZipCodeField

#post database model

class Post(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100,blank=True, help_text='Name of your organization (optional)')
    content = models.TextField(verbose_name="Description")
    date_posted = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to='post_thumbnails',blank=True, help_text="Attach a flyer (optional)")
    attachment = models.FileField(upload_to='attachment', blank=True, help_text="Other attachment (optional)")
    author = models.ForeignKey(User, on_delete=models.CASCADE) #delete post when user get deleted
    phone = PhoneField(help_text='Contact phone number',null= True)
    email = models.EmailField(max_length=70,null= True,help_text="Contact email address")

    address = models.CharField(max_length=150, blank=True,help_text="Location of this activity (optional)")
    city = models.CharField(max_length=150, blank=True)
    state = USStateField(blank=True)
    zip = USZipCodeField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk}) #redirect to the created post


