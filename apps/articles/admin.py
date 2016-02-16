from django.contrib import admin

from apps.articles.forms import ArticleAdminForm
from apps.articles.models import Article, ArticleImage


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = [
        (
            'Title',
            {'fields': (
                'title',
                'slug',
                'published_status',

            )}
        ),
        ('Body', {'classes': ('full-width',), 'fields': ('body',)}),
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

admin.site.register(Article, ArticleAdmin)


class ArticleImageAdmin(admin.ModelAdmin):

    search_fields = ['body', 'name']
    readonly_fields = ['created_at', 'updated_at']

    list_display = (
        'created_at',
        'updated_at'
    )


admin.site.register(ArticleImage, ArticleImageAdmin)
