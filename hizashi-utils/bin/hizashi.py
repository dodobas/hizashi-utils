#!/usr/bin/env python
from django.core import management
import argparse


def initproject(args):
    """
    Initializes Django Hizashi project
    """
    print 'Initializing Django Hizashi project...'

    management.call_command(
        'startproject', args.project_name,
        template=args.template,
        extensions=['.py', '.rst'], verbosity=0)


parser = argparse.ArgumentParser(description='Execute Hizashi utilities')
subparsers = parser.add_subparsers(title='Subcommands')


# initproject options
parser_initproject = subparsers.add_parser(
    'initproject', help='Initializes Django Hizashi project'
)
parser_initproject.add_argument(
    'project_name', type=str, help='Django Project name')
parser_initproject.add_argument(
    '--template', type=str, help='Django Project name',
    default=(
        'https://github.com/dodobas/hizashi-project-template/archive/'
        'master.zip')
)
parser_initproject.set_defaults(func=initproject)

if __name__ == "__main__":
    # parse the args, and call default function
    args = parser.parse_args()
    args.func(args)
