from datetime import timedelta

from django.core.urlresolvers import reverse
from django.test.testcases import TestCase
from django.utils import timezone

from aiki_blog.factories import PostFactory


class IndexViewTestCase(TestCase):
    @staticmethod
    def create_post(publish_delta_days=0):
        post = PostFactory()
        post.published_date = timezone.now() + timedelta(days=publish_delta_days)
        post.save()

        return post

    def test_with_no_post(self):
        """If no posts exist, an appropriate message should be displayed."""
        response = self.client.get(reverse('aiki:index'))

        self.assertContains(response, text='No posts written yet.', status_code=200)
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_with_a_past_post(self):
        """Post in the past should be displayed"""
        post = self.create_post(publish_delta_days=-30)

        response = self.client.get(reverse('aiki:index'))

        self.assertQuerysetEqual(
            response.context['posts'],
            ['{post}'.format(post=repr(post))]
        )

    def test_with_a_future_post(self):
        """Post in the future should not be displayed"""
        self.create_post(publish_delta_days=30)

        response = self.client.get(reverse('aiki:index'))

        self.assertQuerysetEqual(response.context['posts'], [])

    def test_with_a_future_and_a_past_post(self):
        """
        Post in the future should not be displayed,
        while post in the past should be displayed
        """

        # Creates future post
        self.create_post(publish_delta_days=30)

        # Creates past post
        post = self.create_post(publish_delta_days=-30)

        response = self.client.get(reverse('aiki:index'))

        self.assertQuerysetEqual(
            response.context['posts'],
            ['{post}'.format(post=repr(post))]
        )

    def test_with_many_posts_in_the_past(self):
        """
        Posts in the past should be displayed, with latest posts first
        """
        post_1 = self.create_post(publish_delta_days=-10)
        post_2 = self.create_post(publish_delta_days=-1)

        response = self.client.get(reverse('aiki:index'))

        self.assertQuerysetEqual(
            response.context['posts'],
            [
                '{post}'.format(post=repr(post_2)),
                '{post}'.format(post=repr(post_1))
            ]
        )
