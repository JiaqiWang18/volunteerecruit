from django import forms
from .models import Post
# create customized user registration form that inherits from the usercreationform and interacts with the User model

class CreatePost(forms.ModelForm):
    class Meta:
        # nested config, model is the User model, fields are the ones in the form
        model = Post
        fields = ['title','content','attachment']

