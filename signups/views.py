from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib import messages
from .forms import NewSignup
from .models import Post, SignUp
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

            recruiter_html_message=render_to_string("signups/recruiter_signup_notice_template.html",{"post_obj":Post.objects.get(id=pk),"form_info":form.instance})
            recruiter_plain_message = strip_tags(recruiter_html_message)
            send_mail(f"You received a new sign up for {Post.objects.get(id=pk).title}", recruiter_plain_message,  os.environ.get("EMAIL_USER"), [Post.objects.get(id=pk).email],html_message=recruiter_html_message, fail_silently=False)

            messages.success(request, f'Your have successfully signed up {Post.objects.get(id=pk).title}! You will receive an email with the service information.')
            return redirect(f'/post/{pk}/')
    else:
        form = NewSignup()
    return render(request, 'signups/signup.html', {'form': form, 'post_obj': Post.objects.get(id=pk)})

#delete signup view
class SignupDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = SignUp
    success_url = reverse_lazy('my-signups') #redirect to sign up list

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, "You have successfully deleted your sign up")
        return super(SignupDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        signup = self.get_object()
        if self.request.user == signup.author:
            return True
        return False

#update signup view

class SignupUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView): #mixin to avoid one user able to update post of another
    model = SignUp
    fields = ["firstname", "lastname", "email", "phone", "message"]
    success_url = reverse_lazy('my-signups') #redirect to sign up list

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your have successfully updated your sign up')
        return super().form_valid(form)

    def test_func(self):
        signup = self.get_object()
        if self.request.user == signup.author:
            return True
        return False
