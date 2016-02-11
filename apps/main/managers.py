from django.db import models
from django.conf import settings
from django.utils import timezone


class PublishedManager(models.Manager):
    """
    Returns published-model instances only, if any.

    Expects 'is_published' boolean or
            'status' with optional 'published_at'-fields.

    Checks for a simple 'is_published' boolean field, or
    checks for 'status', which should be STATUS_PUBLISHED,
    will then also check for an optional 'published_at' field.

    Returns normal queryset if none of the above can be found.
    """

    def get_queryset(self):
        queryset = super(PublishedManager, self).get_queryset()

        _field_names = self.model._meta.get_fields()

        # check for the simple boolean-field first
        for field in _field_names:
            if field.name == 'is_published':
                return queryset.filter(is_published=True)
            if field.name == 'status':

                # check for the more complex status/published
                queryset = queryset.filter(status=settings.STATUS_PUBLISHED)

                # published_at should be either a DateField or a DateTimeField
                _type = self.model._meta.get_field('published_at')
                if _type is None:
                    return queryset

                _type = _type.get_internal_type()
                if _type == 'DateTimeField':
                    return queryset.filter(
                            published_at__lte=timezone.now())
                if _type == 'DateField':
                    return queryset.filter(
                            published_at__lte=timezone.now().date())

        return queryset
