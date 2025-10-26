from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name= 'post_new.html'
    fields = ['title', 'content', 'author']

class PostEditView(UpdateView):
    model = Post
    template_name= 'post_edit.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name= 'post_delete.html'
    success_url = reverse_lazy('home')