from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models.post import Post


class IndexView(ListView):
    context_object_name = 'posts'
    template_name = 'index.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    context_object_name = 'post'
    model = Post
    template_name = 'post/detail.html'
