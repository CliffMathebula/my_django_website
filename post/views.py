from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post

class HomePageView(ListView):
    model = Post

    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new

class UserCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'