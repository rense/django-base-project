from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()

urlpatterns = [
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
