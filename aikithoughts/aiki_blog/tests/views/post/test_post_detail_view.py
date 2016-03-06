from django.core.urlresolvers import reverse
from django.test.testcases import TestCase

from aiki_blog.factories import PostFactory


class PostDetailViewTestCase(TestCase):
    def test_view_published_post(self):
        post = PostFactory()
        post.publish()

        response = self.client.get(reverse('aiki:post_detail', kwargs={'pk': post.pk}))

        self.assertContains(response=response, text=post.title, status_code=200)
        self.assertContains(response=response, text=post.published_date.strftime('%b %-d, %Y, %-H:%M'))
        self.assertContains(response=response, text=post.text, status_code=200)
