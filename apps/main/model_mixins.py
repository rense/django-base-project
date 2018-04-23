import uuid

from django.db import models
from django.utils import timezone
from django.forms.models import model_to_dict


class HashedKeyModelMixin(models.Model):
    """ Mixin that adds an hashed key called 'key'
        that can be exposed to the outside world.

        This is the one that should be used by DRF serializers!
    """
    key = models.CharField(
        max_length=32,
        db_index=True,
        unique=True,
        null=True,
        editable=False
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.key:  # '' is not unique, NULL is ignored
            self.key = None

        super(HashedKeyModelMixin, self).save(*args, **kwargs)
        if not self.key or self.key is None:
            self.key = uuid.uuid4().hex
            models.Model.save(self, update_fields=['key'])


class CreatedAtModelMixin(models.Model):
    """ Mixes in a created_at field """
    created_at = models.DateTimeField(db_index=True, editable=False)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        return super(CreatedAtModelMixin, self).save(*args, **kwargs)


class UpdatedAtModelMixin(models.Model):
    """ Mixes in an updated_at field """
    updated_at = models.DateTimeField(db_index=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super(UpdatedAtModelMixin, self).save(*args, **kwargs)


class HasChangedMixin(models.Model):
    """ A model mixin that tracks model fields' values and provides a
        useful API to know what fields have been changed.

        To ignore certain fields, add 'ignore_changed_fields' to a model:

        @property
        def ignore_has_changed_fields(self):
            return ['<fieldname>']
    """

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(HasChangedMixin, self).__init__(*args, **kwargs)
        self._set_initial()

    def save(self, *args, **kwargs):
        super(HasChangedMixin, self).save(*args, **kwargs)
        self._set_initial()

    def _set_initial(self):
        self._initial = self._dict

    @property
    def changes(self):
        _current = self._dict
        _changes = []
        for k, v in self._initial.items():
            if v != _current[k]:
                _changes.append((k, (v, _current[k])))
        return dict(_changes)

    @property
    def has_changed(self):
        return bool(self.changes)

    @property
    def changed_fields(self):
        return self.changes.keys()

    @property
    def _dict(self):
        try:
            ignore_fields = self.ignore_has_changed_fields
        except AttributeError:
            ignore_fields = []

        _fields = []

        for field in self._meta.fields:
            if field.name not in ignore_fields:
                _fields.append(field.name)
        return model_to_dict(self, _fields)


class ModelMixinBundle(HashedKeyModelMixin, CreatedAtModelMixin,
                       UpdatedAtModelMixin, HasChangedMixin):
    """ Mixin-bundle with our three base model-mixins
    """

    class Meta:
        abstract = True
