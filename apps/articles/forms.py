from django.forms import ModelForm

from apps.articles.models import Article


class ArticleAdminForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
