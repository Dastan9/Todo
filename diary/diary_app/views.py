from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.utils import timezone

class PostList(ListView): 
    model = Post
    context_object_name = 'posts'

class PostDetail(DetailView): 
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PostCreate(CreateView): 
    model = Post


class PostUpdate(UpdateView): 
    model = Post

class PostDelete(DeleteView): 
    model = Post
# Create your views here.
