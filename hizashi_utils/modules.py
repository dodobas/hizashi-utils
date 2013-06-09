from __future__ import print_function
import os
import sys

from django.core import management

from .utils import is_hizashi_project


def initproject(args):
    """
    Initializes Django Hizashi project
    """
    print(
        'Initializing Django Hizashi project... {}'
        .format(args.project_name),
        end='')

    management.call_command(
        'startproject', args.project_name,
        template=args.template,
        extensions=['.py', '.rst'], verbosity=0)

    print(' ...done')


def initapp(args):
    """
    Initializes Django Hizashi application
    """
    if not(is_hizashi_project()):
        print(
            'Path "{0}", doesn\'t look like a Django Hizashi project folder.\n'
            'Please change your current working directory to the '
            '\'django_project\' folder which is in the root of Hizashi '
            'project folder.'.format(os.getcwd())
        )
        # terminate
        sys.exit(1)

    print(
        'Initializing Django Hizashi application... {}'
        .format(args.application_name),
        end='')

    management.call_command(
        'startapp', args.application_name,
        template=args.template,
        verbosity=0)

    print(' ...done')
    print(
        '\nAdd \'{}\' to INSTALLED_APPS in \'core/settings/project.py\''
        .format(args.application_name))
