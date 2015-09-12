from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


from apps.main.model_mixins import CreatedAtModelMixin, UpdatedAtModelMixin
from apps.articles.managers import ArticleManager


class ArticleImage(CreatedAtModelMixin, UpdatedAtModelMixin):

    image = models.ImageField(upload_to="articleimages/")

    class Meta:
        ordering = ["-created_at"]


class Article(CreatedAtModelMixin, UpdatedAtModelMixin):

    objects = ArticleManager()

    title = models.CharField(max_length=128)
    body = models.TextField()

    slug = models.SlugField(max_length=130)

    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    show_quote = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        _now = timezone.now()
        if self.is_published and not self.published_at:
            self.published_at = _now

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




