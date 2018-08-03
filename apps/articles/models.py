from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from apps.articles.managers import ArticleManager
from apps.main.managers import PublishedManager
from apps.main.model_mixins import CreatedAtModelMixin, UpdatedAtModelMixin


class ArticleImage(CreatedAtModelMixin, UpdatedAtModelMixin):
    image = models.ImageField(upload_to="articleimages/")

    class Meta:
        ordering = ["-created_at"]


class ArticleCategory(CreatedAtModelMixin, UpdatedAtModelMixin):
    objects = models.Manager()
    published = PublishedManager()

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=130, unique=True)

    description = models.TextField(null=True, blank=True)

    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Article Category')
        verbose_name_plural = _('Article Categories')

    def __unicode__(self):
        return self.title


class Article(CreatedAtModelMixin, UpdatedAtModelMixin):
    objects = ArticleManager()
    published = PublishedManager()

    title = models.CharField(max_length=128)
    body = models.TextField()

    slug = models.SlugField(max_length=130)

    category = models.ForeignKey(
        ArticleCategory,
        null=True, blank=True,
        related_name='articles',
        on_delete=models.SET_NULL
    )

    published_status = models.PositiveSmallIntegerField(
        choices=settings.PUBLISHED_STATUS_CHOICES,
        default=settings.PUBLISHED_STATUS_DRAFT
    )
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.published_status == settings.PUBLISHED_STATUS_PUBLISHED:
            if not self.published_at:
                self.published_at = timezone.now()

        if not len(self.slug.strip()):
            self.slug = slugify(self.title)

        _slug = self.slug
        _count = 1

        while True:
            try:
                Article.objects.all().exclude(pk=self.pk).get(slug=_slug)
            except MultipleObjectsReturned:
                pass
            except ObjectDoesNotExist:
                break
            _slug = "%s-%s" % (self.slug, _count)
            _count += 1

        self.slug = _slug
        super(Article, self).save(*args, **kwargs)
