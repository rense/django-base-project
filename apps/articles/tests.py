from django.utils import timezone
from django.conf import settings

from rest_framework import status
from rest_framework.fields import DateTimeField
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.articles.models import Article


class ArticleTestCase(APITestCase):

    def setUp(self):
        self.article = Article.objects.create(
            title=u'Test title',
            body=u'Test article body'
        )

    def _publish_article(self, published_at=None):
        self.article.published_status = settings.PUBLISHED_STATUS_PUBLISHED
        if published_at is not None:
            self.article.published_at = published_at
        self.article.save()

    def test_slug(self):
        """ Test unique slugs
        """
        self.assertEqual(self.article.slug, 'test-title')
        self.another_article = Article.objects.create(
            title=u'Test title',
            body=u'Test article body'
        )
        self.assertEqual(self.another_article.slug, 'test-title-1')

    def test_article_is_unpublished(self):
        """ Test article is actually unpublished/draft
        """
        self.assertEqual(
            self.article.published_status, settings.PUBLISHED_STATUS_DRAFT
        )
        url = reverse('articles-detail', args=[self.article.slug])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_publish_article(self):
        """ Test publishing an article
        """
        self.assertEqual(
            self.article.published_status, settings.PUBLISHED_STATUS_DRAFT
        )
        self._publish_article()

        self.assertEqual(
            self.article.published_status, settings.PUBLISHED_STATUS_PUBLISHED
        )
        self.assertLessEqual(self.article.published_at, timezone.now())

    def test_article_is_published(self):
        """ Test fetching a published article
        """
        self._publish_article()
        url = reverse('articles-detail', args=[self.article.slug])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_is_not_yet_published(self):
        self._publish_article(timezone.now() + timezone.timedelta(hours=1))

        url = reverse('articles-detail', args=[self.article.slug])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_article_list(self):
        """ Test for fetching only published articles
        """
        url = reverse('articles-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, [
                {
                    'slug': u'terms-and-conditions',
                    'title': u'Terms and Conditions',
                    'date_published': u'2015-09-12T16:18:54Z'
                },
                {
                    'slug': u'privacy',
                    'title': u'Privacy',
                    'date_published': u'2015-09-12T16:19:35Z'
                },
            ]
        )

    def test_article_list_after_publishing(self):
        """ Test fetching only published articles after publishing one
        """
        now = timezone.now()
        self._publish_article(now)

        url = reverse('articles-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, [
                {
                    'slug': u'terms-and-conditions',
                    'title': u'Terms and Conditions',
                    'date_published': u'2015-09-12T16:18:54Z'
                },
                {
                    'slug': u'privacy',
                    'title': u'Privacy',
                    'date_published': u'2015-09-12T16:19:35Z'
                },
                {
                    'slug': u'test-title',
                    'title': u'Test title',
                    'date_published': DateTimeField().to_representation(now)
                },
            ]
        )


