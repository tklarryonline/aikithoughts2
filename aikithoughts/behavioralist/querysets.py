from django.db import models
from django.utils import timezone


class PublishableQuerySet(models.query.QuerySet):
    def published(self):
        return self.filter(published_date__lte=timezone.now())

    def newest(self):
        return self.order_by('-published_date')


class PostQuerySet(PublishableQuerySet):
    pass
