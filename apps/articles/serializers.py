from rest_framework import serializers

from apps.articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    date_published = serializers.DateTimeField(source='published_at')

    class Meta:
        model = Article
        fields = (
            'title',
            'body',
            'slug',
            'date_published'
        )


class ArticleListSerializer(serializers.ModelSerializer):

    date_published = serializers.DateTimeField(source='published_at')

    class Meta:
        model = Article
        fields = ('slug', 'title', 'date_published')

