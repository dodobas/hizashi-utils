from __future__ import print_function
import os
import sys

from django.core import management

from .utils import (
    HIZASHI_ID, CHDir,
    get_hizashi_project,
    get_docs_folder,
    get_dev_settings_for_user,
)


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

    # create Hizashi project identification file
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


def makedocs(args):
    """
    Build Project documentation and optionally start a Publish server
    """
    try:
        import sphinx
    except ImportError:
        print(
            'Sphinx package is missing, please install it in your virtualenv'
            'using pip: "pip install Sphinx"')
    docs_path = get_docs_folder()

    with CHDir(docs_path):
        build_result = sphinx.main(
            ['dummy_arg', '-b', args.type, 'source', 'build/html'])

        if build_result:
            # on any error during the build, terminate
            sys.exit(1)

    if args.publish and args.type in ('html', 'dirhtml', 'singlehtml'):
        docs_build_path = os.path.join(docs_path, 'build', args.type)

        # start Publish server
        with CHDir(docs_build_path):
            import SimpleHTTPServer
            import SocketServer

            SocketServer.TCPServer.allow_reuse_address = True
            Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

            httpd = SocketServer.TCPServer((args.host, args.port), Handler)

            print(
                'Publish server address: http://', args.host, ':',
                args.port, sep='')
            print('\nTerminate with CTRL-C\n')
            httpd.serve_forever()


def devserver(args):
    """
    Run Django Hizashi development server
    """
    hizashi_project = get_hizashi_project()

    # set default dev settings
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        get_dev_settings_for_user())

    # override settings if user provided as an argument
    if args.settings:
        os.environ['DJANGO_SETTINGS_MODULE'] = args.settings

    # append project path to sys.path
    sys.path.append(hizashi_project)

    with CHDir(hizashi_project):
        management.call_command(
            'runserver',
            verbosity=0)


def colstatic(args):
    """
    Execute Django collectstatic management command
    """
    hizashi_project = get_hizashi_project()

    # set default dev settings
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        get_dev_settings_for_user())

    # override settings if user provided as an argument
    if args.settings:
        os.environ['DJANGO_SETTINGS_MODULE'] = args.settings

    # append project path to sys.path
    sys.path.append(hizashi_project)

    with CHDir(hizashi_project):
        management.call_command(
            'collectstatic',
            interactive=False,
            clear=True,
            verbosity=0)
