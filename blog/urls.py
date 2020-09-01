from django.urls import path
from .views import PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,SearchView,create_post
from . import views

urlpatterns = [
    #home page
    #path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', create_post, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('about/', views.about, name = 'blog-about'),
    path('', SearchView.as_view(), name='blog-home'),
]
