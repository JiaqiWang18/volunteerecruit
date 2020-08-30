from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post

#views

#home post view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #convention: <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #convention: use object.xxx
    ordering = ['-date_posted']
    paginate_by = 5

#user post list view
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #convention: <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #convention: use object.xxx
    paginate_by = 5
    #get posts with that specific user
    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

#each post view
class PostDetailView(DetailView):
    model = Post

#create post view
class PostCreateView(LoginRequiredMixin,CreateView): #mixin to avoid log in
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#update post view
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView): #mixin to avoid one user able to update post of another
    model = Post
    fields = ['title','content']

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