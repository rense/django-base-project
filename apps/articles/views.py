from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.articles.models import Article, ArticleCategory
from apps.articles.serializers import ArticleCategorySerializer
from apps.articles.serializers import ArticleSerializer


class ArticleViewSet(ReadOnlyModelViewSet):
    model = Article
    lookup_field = 'slug'
    permission_classes = (AllowAny,)

    paginate_by = False

    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.published.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        article = get_object_or_404(self.get_queryset(), slug=kwargs['slug'])
        serializer =  self.get_serializer(instance=article)
        return Response(serializer.data)


class ArticleCategoryViewSet(ReadOnlyModelViewSet):
    model = ArticleCategory
    lookup_field = 'slug'
    permission_classes = (AllowAny,)

    serializer_class = ArticleCategorySerializer

    def get_queryset(self):
        return ArticleCategory.published.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ArticleCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        article_category = get_object_or_404(
            self.get_queryset(), slug=kwargs['slug']
        )
        serializer = ArticleCategorySerializer(instance=article_category)
        return Response(serializer.data)
