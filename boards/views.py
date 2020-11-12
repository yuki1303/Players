from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView
from .models import Post, Comment
from . import models
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostsListView(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-id')

class CreatePostsView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['message']
    success_url = "/boards/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePostsView, self).form_valid(form)

class PostsDetailView(DetailView):
    model = Post

class PostsDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('boards:post')

class CommentCreate(CreateView):
    model = Comment
    fields = ['text',]

    def get_success_url(self):
        return reverse('boards:detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.name = self.request.user.last_name
        form.instance.user = self.request.user
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return super(CommentCreate, self).form_valid(form)

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('boards:post')
