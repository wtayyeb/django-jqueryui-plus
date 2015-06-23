Django jQuery UI Plus
==================

Requirements
------------

    `Django <https://www.djangoproject.com/>`_ 1.3 or later
    `django-appconf`


Installation
------------

::

    $ pip install django-jqueryui-plus


Setup
-----

Just add ``'django.contrib.staticfiles'`` and ``'jqueryui'`` to INSTALLED_APPS in
your settings.py::

    INSTALLED_APPS = (
        # ...

        'django.contrib.staticfiles',
        'jqueryui',

        # ...
    )

Refer to Django `static files <https://docs.djangoproject.com/en/dev/howto/static-files/>`_
documentation to configure and deploy static files.


Usage
-----

You can refer to jquery in your template with::

	{% load jqueryui %}
	{% jqueryui_js %}
	{% jqueryui_js 1.7.2 %}
	{% jqueryui_css 1.7.2 %}
	{% jqueryui_css 1.7.2 redmond %}

