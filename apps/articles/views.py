import json

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.articles.models import Article, ArticleImage
from apps.articles.serializers import ArticleSerializer
from apps.articles.serializers import ArticleListSerializer


class ArticleViewSet(ReadOnlyModelViewSet):
    model = Article
    lookup_field = 'slug'
    permission_classes = (AllowAny,)

    renderer_classes = (TemplateHTMLRenderer, JSONRenderer)

    paginate_by = False

    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter_published()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ArticleListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        article = get_object_or_404(self.get_queryset(), slug=kwargs['slug'])

        if request.accepted_renderer.format == 'html':
            content = {
                'active_menu': kwargs['slug'],
                'article': article,
            }
            return Response(content, template_name='site/article.html')

        # JSONRenderer requires serialized data as normal.
        serializer = ArticleSerializer(instance=article)
        return Response(serializer.data)


@csrf_exempt
@require_POST
@login_required
def upload_article_image(request):
    article_images = []
    for _file in request.FILES.getlist("file"):
        article_image = ArticleImage.objects.create(image=_file)
        article_images.append({"filelink": article_image.image.url})
    return JsonResponse(article_images, safe=False)

@login_required
def recent_article_images(request):
    article_images = []
    for article_image in ArticleImage.objects.all()[:20]:
        article_images.append({
            "thumb": article_image.image.url, "image": article_image.image.url
        })
    return JsonResponse(article_images, safe=False)
