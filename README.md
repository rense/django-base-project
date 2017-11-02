# django-base-project

A base "scaffold" for a new Django (REST) project that some people - but mostly myself - find very handy. 
It's now Python 3 only.

### Features
This heavily resembles my favourite workflow and tools, so some things will differ from 'normal' Django projects.
It contains:
- an 'apps' package directory, with a flattened Django base project structure (no repeating project-name);
- a 'settings' package/directory. Base settings are in settings/__init__.py, and can be overridden/expanded in environment-based settings-files, for example settings/development.py. An environment-file containing the name of the environment is expected. See 'getting started' below. I guess it's a bit like `https://code.djangoproject.com/wiki/SplitSettings#SimplePackageOrganizationforEnvironments`, but simpler.
- a 'main' app, containing useful model-mixins and a default viewset;
- a base 'articles' app - every project seems to need one;
    - The admin uses django-suit-redactor for text-areas; 
    - See apps/articles/forms.py for formatting/editor options 
- a basic 'menus' app, using MPTT for the tree-structure (https://github.com/django-mptt/django-mptt) together with django-suit its SortableModelAdmin;
- a shiny django-suit admin (http://djangosuit.com/):
    - AdminSite override, showing a custom admin 'home' (apps/main/admin_site.py);
    - Basic site-wide 'Latest Actions' admin functionality (not per user);
    - See 'getting started' below for django-suit-redactor problems.
- an admin list-display for the internal django admin-log (extended Latest Actions stuff);
- django-rest-camel for DRF renderers/parsers; automatic camelcase to snake-case (and vice-versa) conversion;
- basic invoke commands for local development (`inv run`!), see tasks.py;


### Requirements/dependencies
Base tools, including django-extensions, django-suit, pip-tools, bpython, invoke, etc;
Check out https://github.com/jazzband/pip-tools if you're unfamiliar with pip-tools. Then have a look at requirements.in for base requirements. 
The default development settings contain mysql-settings. Change to your liking.

- runserver_plus for development, gunicorn for staging/production;


### Getting started
- Create a new virtualenv with Python3: `$ virtualenv --python=python3 <env-name>`;
- Install pip-tools and invoke: `$ pip install pip-tools invoke`;
- Clone/download/archive this repository and cd into it;
- Create your environment file, for instance 'development': `$ echo "development" > environment`;
- Edit the corresponding settings/development to your liking (database-settings, etc...);
- Install base requirements: `$ inv pip`;
- run `$ inv migrate`;


### Notes
- If installing Pillow fails (jpeg required), see https://stackoverflow.com/a/34631976
- Django-suit problems: django-suit-redactor is old! I can't add the latest version of Redactor (10.2.2) because of licensing.
    - Get your own version (http://imperavi.com/redactor) and put its files in apps/articles/static/suit-redactor/;
    - Remove django-suit-redactor from installed-apps.
   
      
### TODO
- Menus app tests
- Replace djang-suit-redactor
