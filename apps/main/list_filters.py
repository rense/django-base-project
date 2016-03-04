from django.utils.translation import gettext as _
from django.contrib.admin import SimpleListFilter
from django.utils.encoding import force_text
from django.conf import settings


class DefaultListFilter(SimpleListFilter):

    all_value = '_all_'

    def queryset(self, request, queryset):
        if self.parameter_name in request.GET:
            if request.GET[self.parameter_name] == self.all_value:
                return queryset
            return queryset.filter(
                **{self.parameter_name:request.GET[self.parameter_name]}
            )
        return queryset.filter(**{self.parameter_name:self.default_value()})

    def choices(self, _class):
        yield {
            'selected': self.value() == self.all_value,
            'query_string': _class.get_query_string(
                {self.parameter_name: self.all_value}, []
            ),
            'display': _('All'),
        }
        for lookup, title in self.lookup_choices:
            selected = False
            if self.value() is None:
                if force_text(self.default_value()) == force_text(lookup):
                    selected = True
            elif self.value() == force_text(lookup):
                selected = True

            yield {
                'selected': selected,
                'query_string': _class.get_query_string(
                    {self.parameter_name: lookup}, []
                ),
                'display': title,
            }

    def default_value(self):
        raise NotImplementedError()


class PublishedListFilter(DefaultListFilter):
    """ An admin list-filter that will default to listing published items.
    """
    title = 'Status '

    def __init__(self, request, params, model, model_admin):
        _field_names = model._meta.get_fields()
        for field in _field_names:
            if field.name == 'is_published':
                self.parameter_name = 'is_published'
            if field.name == 'published_status':
                self.parameter_name = 'published_status'
        super(PublishedListFilter, self).__init__(
            request, params, model, model_admin
        )

    def lookups(self, request, model_admin):
        if self.parameter_name == 'published_status':
            return settings.PUBLISHED_STATUS_CHOICES
        return ('_all', 'All'), (1, 'Published only'), (0, 'Unpublished only')

    def default_value(self):
        if self.parameter_name == 'published_status':
            return settings.PUBLISHED_STATUS_PUBLISHED
        return 1


