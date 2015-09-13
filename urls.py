from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from apps.articles.views import ArticleViewSet

admin.autodiscover()

router = routers.SimpleRouter()
router.register(r'api/articles', ArticleViewSet, base_name='articles')

urlpatterns = router.urls

urlpatterns += [

    url(r'^admin/', include(admin.site.urls)),


    # 'secret' article-image urls
    url(r"^admin/articleimages/upload/$",
        'apps.articles.views.upload_article_image',
        name="upload_article_image"
    ),
    url(r"^admin/articleimages/recent/$",
        'apps.articles.views.recent_article_images',
        name="recent_article_images"
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
