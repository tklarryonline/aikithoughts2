from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models.post import Post


class IndexView(ListView):
    queryset = Post.objects.order_by('-published_date')
    context_object_name = 'posts'
    template_name = 'index.html'


class PostDetailView(DetailView):
    context_object_name = 'post'
    model = Post
    template_name = 'post/detail.html'
