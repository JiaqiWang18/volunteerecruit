from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib import messages
from .forms import NewSignup
from .models import Post
import os

def create_signup(request,pk):
    if (request.user.is_anonymous):
        messages.warning(request, f"To better organize your sign ups, you can login or register for an account.")

    if request.method == 'POST':
        form = NewSignup(request.POST)
        if (request.user.is_anonymous == False):
            #link user obj with the sign ups
            form.instance.author = request.user
        if form.is_valid():
            # file is saved
            form.instance.post = Post.objects.get(id=pk)
            form.save()
            html_message = render_to_string("signups/signup_notice_template.html",{"post_obj":Post.objects.get(id=pk),"form_info":form.instance})
            plain_message = strip_tags(html_message)
            send_mail(f"Your new volunteer sign up for {Post.objects.get(id=pk).title}", plain_message,  os.environ.get("EMAIL_USER"), [form.instance.email],html_message=html_message, fail_silently=False)
            messages.success(request, f'Your have scuccessfully signed up for {Post.objects.get(id=pk).title}! You will receive an email with the service information.')
            return redirect(f'/post/{pk}/')
    else:
        form = NewSignup()
    return render(request, 'signups/signup.html', {'form': form, 'post_obj': Post.objects.get(id=pk)})