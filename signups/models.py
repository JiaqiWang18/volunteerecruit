from django.db import models
from phone_field import PhoneField
from blog.models import Post
from django.contrib.auth.models import User

class SignUp(models.Model):
    firstname = models.CharField(max_length=100,verbose_name="First Name")
    lastname = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(max_length=70,null= True,help_text="Contact email address")
    phone = PhoneField(help_text='Contact phone number',null= True, blank = True)
    message = models.TextField(help_text="Message to the recruitor",null=True, blank=True)

    #relationships
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}'s signup for {self.post.title}"