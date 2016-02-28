from django.conf.urls import url

from .views.index_view import IndexView
from .views.post.post_detail_view import PostDetailView

app_name = 'aiki'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='post_detail')
]
