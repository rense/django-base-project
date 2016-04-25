from django.core.exceptions import FieldDoesNotExist
from django.db import models
from django.conf import settings
from django.utils import timezone


def get_published(queryset):

    meta = queryset.model._meta

    try:
        # Check for the simple boolean-field first
        meta.get_field('is_published')
        return queryset.filter(is_published=True)
    except FieldDoesNotExist:
        try:
            # Check for the more complex status/published
            meta.get_field('published_status')
        except FieldDoesNotExist:
            # No published fields found. To be safe, return nothing
            raise Exception("No published fields found")

    queryset = queryset.filter(
        published_status=settings.PUBLISHED_STATUS_PUBLISHED
    )
    try:
        # Field published_at could be a DateField or a DateTimeField
        _type = meta.get_field('published_at')
    except FieldDoesNotExist:
        # Published as is
        return queryset

    _type = _type.get_internal_type()
    if _type == 'DateTimeField':
        return queryset.filter(published_at__lte=timezone.now())
    if _type == 'DateField':
        return queryset.filter(published_at__lte=timezone.now().date())
    raise Exception("Published fields of unknown type")


class PublishedManager(models.Manager):
    """
    Returns published-model instances only, if any.

    Expects 'is_published' boolean or
            'published_status' with optional 'published_at'-fields.

    Checks for a simple 'is_published' boolean field, or
    checks for 'published_status', which should be STATUS_PUBLISHED,
    will then also check for an optional 'published_at' field.

    Raises exceptions if fields are not found
    """
    def get_queryset(self):
        queryset = super(PublishedManager, self).get_queryset()
        return get_published(queryset)

