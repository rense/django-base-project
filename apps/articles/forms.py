from django.forms import ModelForm
from suit.widgets import SuitSplitDateTimeWidget
from suit_redactor.widgets import RedactorWidget

from apps.articles.models import Article


class ArticleAdminForm(ModelForm):

    class Meta:
        model = Article

        fields = '__all__'

        widgets = {
            'body': RedactorWidget(
                editor_options={
                    'rows': 120,
                    'plugins': ['imagemanager'],

                    # TODO: make this work...
                    # 'imageUpload': reverse('upload_article_image'),
                    # 'imageGetJson': reverse('recent_article_images'),

                    'imageUpload': '/admin/articleimages/upload/',
                    'imageManagerJson': '/admin/articleimages/recent/',

                    'imageFloatMargin': '40px',

                    'formatting': [],
                    'formattingAdd': [
                        {'tag': 'h2', 'title': 'Title'},
                        {'tag': 'p', 'title': 'Paragraph'},
                    ]
                },

            ),
            'published_at': SuitSplitDateTimeWidget
        }

    class Media:
        js = ('suit-redactor/redactor/plugins/imagemanager/imagemanager.js',)
