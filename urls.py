from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from apps.articles.views import ArticleViewSet, ArticleCategoryViewSet
from apps.articles.views import upload_article_image, recent_article_images
from apps.menus.views import MenuViewSet

admin.autodiscover()

router = routers.DefaultRouter()

router.register(r'articles', ArticleViewSet, base_name='articles')

router.register(
    r'articlecategories',
    ArticleCategoryViewSet,
    base_name='article-categories'
)

router.register(r'menus', MenuViewSet, base_name='menus')


urlpatterns = [

    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),

    # 'secret' article-image urls
    url(r"^admin/articleimages/upload/$",
        upload_article_image, name="upload_article_image"
    ),
    url(r"^admin/articleimages/recent/$",
        recent_article_images, name="recent_article_images"
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
