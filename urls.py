from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from apps.articles.views import ArticleViewSet, ArticleCategoryViewSet
from apps.menus.views import MenuViewSet

admin.site.site_header = settings.SITE_ADMIN_TITLE

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
    url(r'^api/login/', obtain_jwt_token),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
