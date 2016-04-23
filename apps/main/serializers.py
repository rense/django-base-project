from rest_framework import serializers

from django.utils import timezone
from django.conf import settings


class PublishedListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(
            published_status=settings.PUBLISHED_STATUS_PUBLISHED,
            published_at__lte=timezone.now()
        )
        return super(PublishedListSerializer, self).to_representation(data)


class RecursiveField(serializers.Serializer):
    """
    """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
