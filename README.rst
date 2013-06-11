Django Hizashi project utilities
================================

A set of command line helper utilities for managing Django Hizashi project
environment.

About the project
-----------------

Django Hizashi is a Django project environment based on iterating personal
best practices. Management commands recreate familiar project directory
structure from prepared `project <https://github.com/dodobas/hizashi-project-
template>`_ and `application <https://github.com/dodobas/hizashi-application-
template>`_ templates.

Utilities are context aware, so as long as you are in a subdirectory of the
main Django Hizashi project folder, script utilities will work on best effort
basis.

Quick start
-----------

* create and initialize a new Python virtual environment
* install hizashi-utils: ``pip install hizashi-utils``
* initialize project: ``hizashi.py initproject my_new_project``
* change directory to that project: ``cd my_new_project``
* initialize an application: ``hizashi.py initapp my_new_app``


Project level utilities
-----------------------

initproject
^^^^^^^^^^^

To initialize a new project execute:

    hizashi.py initproject my_new_project_name

Optional parameters:

* *template* - path or url for a Django project template, defaults to https://github.com/dodobas/hizashi-project-template/archive/master.zip


makedocs
^^^^^^^^

To builds Sphinx docs execute:

    hizashi.py makedocs

Optional parameters:

* *type* - documentation type, defaults to *html*, mimics sphinx Makefile
* *publish* - switch to activate the Publish server, a documentation HTTP server
* *host* - Publish server host, defaults to '127.0.0.1'
* *port* - Publish server port, defaults to '54299'


Application level utilities
---------------------------

initapp
^^^^^^^

To initialize a new application execute:

    hizashi.py initapp my_new_application_name

Optional parameters:

* *template* - path or url for a Django application template, defaults to https://github.com/dodobas/hizashi-application-template/archive/master.zip
