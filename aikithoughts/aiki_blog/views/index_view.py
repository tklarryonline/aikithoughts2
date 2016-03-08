from django.views.generic import ListView

from ..models import Post


class IndexView(ListView):
    context_object_name = 'posts'
    template_name = 'index.html'

    def get_queryset(self):
        return Post.objects.published().newest()
