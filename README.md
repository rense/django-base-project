# django-base-project

My base "scaffold" for a new Django (REST) project that some people - but mostly I myself - find very handy. 

### Features
This heavily resembles my favourite workflow and tools, so some things will differ from 'normal' Django projects.
It contains:
- an 'apps' package directory, with a flattened Django base project structure (no repeating project-name, can't stand it);
- a 'settings' package/directory. Base settings are in settings/__init__.py, and can be overridden/expanded in environment-based settings-files, for example settings/development.py. An environment-file containing the name of the environment is expected. See 'getting started' below. I guess it is a bit like a bit like `https://code.djangoproject.com/wiki/SplitSettings#SimplePackageOrganizationforEnvironments`, but simpler.
- a 'main' app, containing useful model-mixins and a default viewset;
- a base 'articles' app - every project seems to need one;
    - The admin uses django-suit-redactor for text-areas; 
    - Has a couple of (fake) fixtures to get started with;
    - See apps/articles/forms.py for formatting/editor options 

- a shiny django-suit admin (http://djangosuit.com/):
    - AdminSite override, showing a custom admin 'home' (apps/main/admin_site.py);
    - Basic site-wide 'Latest Actions' admin functionality (not per user);
    - See 'getting started' below for django-suit-redactor problems.
- an admin list-display for the internal django admin-log (extended Latest Actions stuff);

- basic fabric commands for local development (`fab run`!), see fabfile.py;


### Requirements/dependencies
My base tools, including django-extensions, django-suit, pip-tools, bpython, fabric, etc;
Check out https://github.com/nvie/pip-tools if you're unfamiliar with pip-tools. Then have a look at requirements.in for base requirements. 
The default development settings contain mysql-settings, because I'm old like that. Change to your likings obviously.

- runserver_plus for development, gunicorn for staging/production;


### Getting started
- Create a new virtualenv;
- Install pip-tools: `$ pip install pip-tools`;
- Clone/download/archive this and cd into it;
- Create an environment file: `$ echo "development" > environment`. This is added to .gitignore;
- Edit settings/development to your liking (database-settings, etc...);
- Install base requirements: `$ pip-sync`;

- Django-suit problems: django-suit-redactor is old! I can't add the latest version of Redactor (10.2.2) because of licensing terms.
    - Get your own version (http://imperavi.com/redactor) and put its files in apps/articles/static/suit-redactor/;
    - Remove django-suit-redactor from installed-apps;
    
   
