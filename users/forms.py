from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# create customized user registration form that inherits from the usercreationform and interacts with the User model
class UserRegisterForm (UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        # nested config, model is the User model, fields are the ones in the form
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        # nested config, model is the User model, fields are the ones in the form
        model = User
        fields = ['username','first_name','last_name','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','image']