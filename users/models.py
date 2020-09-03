from django.db import models
from django.contrib.auth.models import User

# Profile pic model
class Profile(models.Model):
    # add other rleative fields
    user = models.OneToOneField(User,on_delete=models.CASCADE) #relate profile to the user
    bio = models.CharField(max_length=100,blank=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    # resize img to smaller
    '''
    def save(self,*args,**kwargs):
    super().save(**kwargs)
    img = Image.open(self.image.path)
    if img.height > 300 or img.width > 300:
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.image.path)
    '''
