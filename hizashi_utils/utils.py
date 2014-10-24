from __future__ import print_function
import os
import sys

import django
from django.core import management

HIZASHI_ID = '.hizashi_project'


class CHDir:
    """
    Context manager for directory change operation
    """
    def __init__(self, newPath):
        self.newPath = newPath

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def is_writable(path):
    """
    Checks if a path exists and it's writeable by current user
    """
    if os.path.exists(path) and os.access(path, os.W_OK):
        return True
    else:
        print(
            'Path "{0}" is not writeable by the current user or it doesn\'t '
            'exist.'.format(path)
        )
        # terminate
        sys.exit(1)


def is_file(path):
    """
    Checks if a path exists and it's a file
    """
    if os.path.exists(path) and os.path.isfile(path):
        return True
    else:
        return False


def get_docs_folder():
    """
    Returns docs path of a Django Hizashi project
    """
    root_path = get_hizashi_root()

    docs_path = os.path.join(root_path, 'docs')
    return docs_path if is_writable(docs_path) else None


def get_hizashi_project():
    """
    Returns root path of a Django Hizashi project
    """
    root_path = get_hizashi_root()

    project_path = os.path.join(root_path, 'django_project')
    return project_path if is_writable(project_path) else None


def get_hizashi_root():
    """
    Searches for Django Hizashi project root

    returns 'path'
    """
    cur_dir = os.getcwd()
    while cur_dir != '/':
        if is_file(os.path.join(cur_dir, HIZASHI_ID)):
            # return hizashi project root
            return cur_dir
        else:
            # go back one folder
            cur_dir = os.path.normpath(os.path.join(cur_dir, '..'))
    else:
        print(
            'Path "{0}" is not a subdirectory of a Django Hizashi project.\n'
            'Please change your current working directory to a Django '
            'Hizashi project folder.'.format(os.getcwd())
        )
        # terminate
        sys.exit(1)


def get_dev_settings_for_user():
    """
    Returns development settings module

    Function actually checks if a developer specific settings module exists.
    For example, a system user 'philip' will have the 'dev_philip.py'
    settings module.

    If there is no developer specific settings, fallback to the 'dev.py'
    """
    # try to pick up currently logged in user dev settings
    user = os.getlogin()
    user_settings = 'dev_{}.py'.format(user)

    project_path = get_hizashi_project()

    user_dev_settings = os.path.join(
        project_path, 'core', 'settings', user_settings
    )

    if is_file(user_dev_settings):
        return 'core.settings.dev_{}'.format(user)
    else:
        # return default settings
        return 'core.settings.dev'


def get_test_settings_for_user():
    """
    Returns test settings module

    Function actually checks if a developer specific settings module exists.
    For example, a system user 'philip' will have the 'test_philip.py'
    settings module.

    If there is no developer specific settings, fallback to the 'test.py'
    """
    # try to pick up currently logged in user dev settings
    user = os.getlogin()
    user_settings = 'test_{}.py'.format(user)

    project_path = get_hizashi_project()

    user_test_settings = os.path.join(
        project_path, 'core', 'settings', user_settings
    )

    if is_file(user_test_settings):
        return 'core.settings.test_{}'.format(user)
    else:
        # return default settings
        return 'core.settings.test'


def run_command_in_prod(cli_args, command, *args, **kwargs):
    """
    Executes Django management command using prod settings
    """
    # set default dev settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.prod')

    # override settings if user provided as an argument
    if cli_args.settings:
        os.environ['DJANGO_SETTINGS_MODULE'] = cli_args.settings

    run_command(command, *args, **kwargs)


def run_command_in_dev(cli_args, command, *args, **kwargs):
    """
    Executes Django management command using dev settings
    """
    # set default dev settings
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        get_dev_settings_for_user()
    )

    # override settings if user provided as an argument
    if cli_args.settings:
        os.environ['DJANGO_SETTINGS_MODULE'] = cli_args.settings

    run_command(command, *args, **kwargs)


def run_command_in_test(cli_args, command, *args, **kwargs):
    """
    Executes Django management command using test settings
    """
    # set default dev settings
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        get_test_settings_for_user()
    )

    # override settings if user provided as an argument
    if cli_args.settings:
        os.environ['DJANGO_SETTINGS_MODULE'] = cli_args.settings

    run_command(command, *args, **kwargs)


def run_command(command, *args, **kwargs):
    """
    Executes Django management command using test settings
    """
    hizashi_project = get_hizashi_project()

    # append project path to sys.path
    sys.path.append(hizashi_project)

    # initialize django
    django.setup()

    with CHDir(hizashi_project):
        management.call_command(command, *args, **kwargs)
