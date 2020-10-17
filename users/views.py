from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from signups.models import SignUp
from blog.models import Post

# register form view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #save user to db!
            username = form.cleaned_data.get("username")
            messages.success(request,f'Your account {username} has been created! You can now start recruiting!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

def public_profile(request):
    return render(request, 'users/public_profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {"u_form":u_form, "p_form":p_form}


    return render(request,'users/profile.html',context)

@login_required
def manage_recruitments(request):
    contact_list = Post.objects.filter(author=request.user).order_by('-date_posted')
    paginator = Paginator(contact_list, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {"page_obj":page_obj}

    return render(request,'users/manage_recruitments.html',context)

@login_required
def manage_signups(request):
    contact_list = SignUp.objects.filter(author=request.user)
    paginator = Paginator(contact_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {"page_obj":page_obj}

    return render(request,'users/manage_signups.html',context)