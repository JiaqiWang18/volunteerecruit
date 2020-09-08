from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post
from .forms import CreatePost
#blog app views

#home post view
class SearchView(ListView):
    model = Post
    template_name = 'blog/post_search.html'
    context_object_name = 'all_search_results'
    paginate_by = 5

    def get_queryset(self):
        #result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Post.objects.filter(title__icontains=query).order_by('-date_posted')
            result = postresult
        else:
            postresult = Post.objects.all().order_by('-date_posted')
            result = postresult
        return result
#home without search
'''
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #convention: <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #convention: use object.xxx
    ordering = ['-date_posted']
    paginate_by = 5
'''


#user post list view
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #convention: <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #convention: use object.xxx
    paginate_by = 5
    #get posts with that specific user
    def get_queryset(self):
        post_user=get_object_or_404(User, username=self.kwargs.get('username'))
        print(post_user.first_name)
        return Post.objects.filter(author=post_user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_user = get_object_or_404(User, username=self.kwargs.get('username'))
        context["first_name"] = post_user.first_name
        context["last_name"] = post_user.last_name
        context["email"] = post_user.email
        context["bio"] = post_user.profile.bio
        context["profile_image_url"] = post_user.profile.image.url
        return context

#each post view
class PostDetailView(DetailView):
    model = Post

#create post view
'''
class PostCreateView(LoginRequiredMixin,CreateView): #mixin to avoid log in
    model = Post
    fields = ['title','content','thumbnail','attachment','address']

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)

'''
@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.instance.author = request.user
            print(request.FILES)
            form.save()
            return redirect('blog-home')
    else:
        form = CreatePost()
    return render(request, 'blog/post_form.html', {'form': form})


#update post view
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView): #mixin to avoid one user able to update post of another
    model = Post
    fields = ['title', 'organization', 'content', 'email', 'phone', 'address', 'city', 'state', 'zip', 'thumbnail', 'attachment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#delete post view
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #redirect to home page

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


#about page
def about(request):
    return render(request, 'blog/about.html',{'title':'about'})

