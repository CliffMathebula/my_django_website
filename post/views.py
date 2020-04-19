from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Post

    template_name = 'home.html'
    context_object_name = 'all_users_list'  # new


class UserCreateView(CreateView):  # new
    model = Post
    template_name = 'add_user.html'
    fields = '__all__'


class UserDetailsView(DetailView):
    model = Post
    template_name = 'user_details.html'


class EditDetailsView(UpdateView):
    model = Post
    template_name = 'update_details.html'

    fields = ['name', 'surname']


class DeleteUserView(DeleteView):
    model = Post
    template_name = 'user_delete.html'
    success_url = reverse_lazy('home')
