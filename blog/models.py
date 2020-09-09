from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from phone_field import PhoneField
from localflavor.us.models import USStateField,USZipCodeField
import requests
import os
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

    address = models.CharField(max_length=150, help_text="Location of this activity (optional)")
    city = models.CharField(max_length=150)
    state = USStateField()
    zip = USZipCodeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    #geocode upon saving
    def save(self):
        if not self.latitude or not self.longitude:
            current_address = f"{self.address} {self.city}, {self.state}"
            self.latitude, self.longitude = self.geocode(current_address)
        super(Post, self).save()

    def geocode(self,address):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {'sensor': 'false', 'address': address, 'key': os.environ.get("GOOGLE_MAP_API_KEY")}
        r = requests.get(url, params=params)
        results = r.json()['results']
        location = results[0]['geometry']['location']
        return location['lat'], location['lng']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk}) #redirect to the created post


