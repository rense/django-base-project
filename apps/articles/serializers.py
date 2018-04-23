from rest_framework import serializers

from apps.articles.models import Article, ArticleCategory
from apps.main.serializers import PublishedListSerializer


class ArticleSerializer(serializers.ModelSerializer):

    date_published = serializers.DateTimeField(source='published_at')
    category = serializers.SerializerMethodField()

    ist_serializer_class = PublishedListSerializer

    class Meta:
        model = Article
        fields = (
            'category',
            'title',
            'body',
            'slug',
            'date_published'
        )

    def get_category(self, article):
        if article.category:
            return article.category.slug
        return None



class ArticleCategorySerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(read_only=True, many=True)

    class Meta:
        model = ArticleCategory
        fields = (
            'title',
            'slug',
            'articles'
        )
