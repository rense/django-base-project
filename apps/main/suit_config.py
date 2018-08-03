from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'

    menu = (
        ParentItem('Accounts', children=[
            ChildItem(model='auth.user'),
        ]),
        ParentItem('Content', children=[
            ChildItem(model='articles.article'),
            ChildItem(model='articles.articlecategory'),
        ]),
        ParentItem('Misc', children=[
            ChildItem('Admin Log', model='admin.logentry'),
            ChildItem(model='sites.site'),
            ChildItem('Media', model='filer.folder'),
        ]),
    )

    def ready(self):
        super(SuitConfig, self).ready()
