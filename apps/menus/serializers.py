from django.conf import settings
from rest_framework import serializers

from apps.menus.models import MenuItem
from apps.main.serializers import RecursiveField


class MenuItemSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, required=True)
    target = serializers.SerializerMethodField()

    _choices = dict(
        (index, name) for index, name in settings.MENU_TARGET_CHOICES
    )

    class Meta:
        model = MenuItem
        fields = (
            'title',
            'url',
            'children',
            'target',
        )

    def get_target(self, obj):
        return self._choices[obj.target]
