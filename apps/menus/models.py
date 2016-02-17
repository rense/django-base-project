from django.db import models
from django.conf import settings

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from apps.menus.managers import MenuItemManager
from apps.main.managers import PublishedManager


class MenuItem(MPTTModel):
    """
    """
    objects = MenuItemManager()
    published = PublishedManager()

    title = models.CharField(max_length=150)
    url = models.CharField(max_length=400, null=True, blank=True)

    parent = TreeForeignKey(
        'self', null=True, blank=True,
        related_name='children'
    )

    target = models.PositiveSmallIntegerField(
        choices=settings.MENU_TARGET_CHOICES,
        default=settings.MENU_TARGET_SELF
    )

    sort_order = models.PositiveIntegerField()
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
        ordering = ['sort_order']

    class MPTTMeta:
        order_insertion_by = ['sort_order']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(MenuItem, self).save(*args, **kwargs)
        MenuItem.objects.rebuild()



