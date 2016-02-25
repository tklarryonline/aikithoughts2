from django.core.urlresolvers import reverse
from django.test.testcases import TestCase


class IndexViewTestCase(TestCase):
    def test_index_view_with_no_post(self):
        """If no posts exist, an appropriate message should be displayed."""
        response = self.client.get(reverse('aiki:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No posts written yet.')
        self.assertQuerysetEqual(response.context['posts'], [])
