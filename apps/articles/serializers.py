from rest_framework import serializers

from apps.articles.models import Article, ArticleCategory
from apps.main.serializers import PublishedListSerializer


class ArticleSerializer(serializers.ModelSerializer):

    date_published = serializers.DateTimeField(source='published_at')
    category = serializers.SlugField(source='category.slug')

    class Meta:
        model = Article
        fields = (
            'category',
            'title',
            'body',
            'slug',
            'date_published'
        )


class ArticleListSerializer(serializers.ModelSerializer):

    date_published = serializers.DateTimeField(source='published_at')
    category = serializers.SlugField(source='category.slug')

    class Meta:
        model = Article
        list_serializer_class = PublishedListSerializer

        fields = (
            'slug',
            'title',
            'category',
            'date_published'
        )


class ArticleCategorySerializer(serializers.ModelSerializer):

    articles = ArticleListSerializer(read_only=True, many=True)

    class Meta:
        model = ArticleCategory
        fields = (
            'title',
            'slug',
            'articles'
        )
