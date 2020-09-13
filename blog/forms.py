from django import forms
from .models import Post

class DateTime(forms.DateTimeInput):
    input_type = "datetime-local"


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','organization','content','start_time','end_time','email','phone','address','city','state','zip','thumbnail','attachment']
        widgets = {
            'start_time': DateTime(),
            'end_time': DateTime()
        }

