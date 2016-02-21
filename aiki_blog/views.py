from django.views.generic.list import ListView

from .models.post import Post


class PostListView(ListView):
    queryset = Post.objects.order_by('-published_date')
    context_object_name = 'posts'
