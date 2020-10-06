from django.shortcuts import render, redirect
from .forms import NewSignup
from .models import Post

# Create your views here.
def create_signup(request,pk):
    if request.method == 'POST':
        form = NewSignup(request.POST)
        if form.is_valid():
            # file is saved
            form.instance.post = Post.objects.get(id=pk)
            form.save()
            return redirect(f'/post/{pk}/')
    else:
        form = NewSignup()
    return render(request, 'signups/signup.html', {'form': form})