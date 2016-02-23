from django.test.testcases import TestCase

from aiki_blog.models.post import Post


class PostTestCase(TestCase):
    def test_string_representative(self):
        post = Post(title='Some random title')
        self.assertEqual(str(post), post.title)
