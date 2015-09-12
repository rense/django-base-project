from django.db import models
from django.db.models import Q

from django.utils import timezone


class ArticleManager(models.Manager):

    def filter_published(self):
        return self.filter(
            Q(is_published=True),
            Q(published_at__lte=timezone.now())
        )
