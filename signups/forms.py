from django import forms
from .models import SignUp

class NewSignup(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["firstname","lastname","email","phone","message"]

