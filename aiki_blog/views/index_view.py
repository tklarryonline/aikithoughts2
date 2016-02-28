from django.utils import timezone
from django.views.generic import ListView

from ..models import Post


class IndexView(ListView):
    context_object_name = 'posts'
    template_name = 'index.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
