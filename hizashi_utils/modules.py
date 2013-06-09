from __future__ import print_function
from django.core import management


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
