# Configuration for django-suit.
# Can become quite large, hence its own file.

SUIT_CONFIG = {
    'ADMIN_NAME': 'Administration Dashboard',
    'CONFIRM_UNSAVED_CHANGES': False,
    'SEARCH_URL': '',  # hide

    'MENU_OPEN_FIRST_CHILD': True,

    'MENU': (
        {
            'label': 'User Management',
            'icon': 'icon-user',
            'models': (
                'auth.user',

            )
        },
        {
            'label': 'Content Management',
            'icon': 'icon-font',
            'models': (
                'articles.article',
            )
        },
        '-',
        {
            'label': 'System Management',
            'icon': 'icon-cog',
            'models': (
                {'model': 'contact.subject', 'label': 'Contact-form subjects'},
                {'model': 'admin.logentry', 'label': 'Admin Log'},

            )
        },
    )

}