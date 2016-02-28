from datetime import datetime
from unittest.case import TestCase
from unittest.mock import patch

from aiki_blog.factories import PostFactory


class PostTestCase(TestCase):
    def test_string_representative(self):
        post = PostFactory()
        self.assertEqual(str(post), post.title)

    @patch('aiki_blog.models.post.timezone.now')
    def test_publish(self, mock_timezone_now):
        expected_published_date = datetime.utcnow()
        mock_timezone_now.return_value = expected_published_date

        post = PostFactory()
        post.publish()

        self.assertEqual(post.published_date, expected_published_date)
