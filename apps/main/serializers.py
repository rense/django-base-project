from rest_framework import serializers

from apps.main.managers import get_published


class PublishedListSerializer(serializers.ListSerializer):
    """ DRF ListSerializer that returns published items
    """

    def to_representation(self, data):
        data = get_published(data)
        return super(PublishedListSerializer, self).to_representation(data)


class RecursiveField(serializers.Serializer):
    """
    """

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
