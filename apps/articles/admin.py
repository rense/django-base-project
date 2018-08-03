from django.contrib import admin

from apps.articles.forms import ArticleAdminForm
from apps.articles.models import Article, ArticleCategory
from apps.main.list_filters import PublishedListFilter


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = [
        (
            'Title',
            {'fields': (
                'title',
                'slug',
                'category',
                'published_status',
            )}
        ),
        ('Body', {'classes': ('full',), 'fields': ('body',)}),
        ('Dates', {'fields': ('published_at', 'created_at', 'updated_at')}),
    ]

    list_display = (
        'title',
        'slug',
        'published_status',
        'published_at',
        'created_at',
        'updated_at'
    )
    list_display_links = ('title',)
    list_filter = (PublishedListFilter,)


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}

    list_display = (
        'title', 'slug', 'is_published'
    )

    fieldsets = [
        (
            'Title',
            {'fields': (
                'title',
                'slug',
                'is_published',
                'description',
            )}
        ),
    ]
