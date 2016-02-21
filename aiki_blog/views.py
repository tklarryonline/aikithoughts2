from django.views.generic.list import ListView

from .models.post import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
