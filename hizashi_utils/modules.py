from __future__ import print_function
import os
import sys

from django.core import management

from .utils import HIZASHI_ID, get_hizashi_project, CHDir


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

    project_folder = os.path.join(os.getcwd(), args.project_name)
    project_identifier = os.path.join(project_folder, HIZASHI_ID)
    with open(project_identifier, 'wb') as proj_file:
        proj_file.write(
            "DO NOT DELETE\n\n"
            "Django Hizashi project identifier.\n\n"
            "DO NOT DELETE\n")

    print(' ...done')


def initapp(args):
    """
    Initializes Django Hizashi application
    """
    hizashi_project = get_hizashi_project()

    print(
        'Initializing Django Hizashi application... {}'
        .format(args.application_name),
        end='')

    with CHDir(hizashi_project):
        management.call_command(
            'startapp', args.application_name,
            template=args.template,
            verbosity=0)

    print(' ...done')
    print(
        '\nAdd \'{}\' to INSTALLED_APPS in \'core/settings/project.py\''
        .format(args.application_name))
