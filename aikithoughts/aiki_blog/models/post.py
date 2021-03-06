from django.db import models
from django.utils import timezone

from behavioralist.behaviors.excerptable import Excerptable
from behavioralist.querysets import PostQuerySet


class Post(Excerptable, models.Model):
    author = models.ForeignKey(to='auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
