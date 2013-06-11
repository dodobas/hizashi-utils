#!/usr/bin/env python
import argparse

from hizashi_utils import modules

parser = argparse.ArgumentParser(description='Execute Hizashi utilities')
subparsers = parser.add_subparsers(title='Subcommands')


# initproject options
parser_initproject = subparsers.add_parser(
    'initproject', help='Initializes Django Hizashi project'
)
parser_initproject.add_argument(
    'project_name', type=str, help='Django Project name')
parser_initproject.add_argument(
    '--template', type=str, help='Django Project template folder/archive',
    default=(
        'https://github.com/dodobas/hizashi-project-template/archive/'
        'master.zip')
)
parser_initproject.set_defaults(func=modules.initproject)

# initapp options
parser_initapp = subparsers.add_parser(
    'initapp', help='Initializes Django Hizashi application'
)
parser_initapp.add_argument(
    'application_name', type=str, help='Application name')
parser_initapp.add_argument(
    '--template', type=str, help='Application template folder/archive',
    default=(
        'https://github.com/dodobas/hizashi-application-template/archive/'
        'master.zip')
)
parser_initapp.set_defaults(func=modules.initapp)

# makedocs options
parser_makedocs = subparsers.add_parser(
    'makedocs', help='Builds Django Hizashi documentation'
)
parser_makedocs.add_argument(
    '--type', type=str, help='Sphinx documentation target (default: html)',
    default='html'
)
parser_makedocs.add_argument(
    '--publish', help=(
        'Start publish server, a documentation HTTP server'),
    action='store_true'
)
parser_makedocs.add_argument(
    '--host', type=str, help='Publish server host (default: 127.0.0.1)',
    default='127.0.0.1'
)
parser_makedocs.add_argument(
    '--port', type=int, help='Publish server port (default: 54299)',
    default=54299
)
parser_makedocs.set_defaults(func=modules.makedocs)


if __name__ == "__main__":
    # parse the args, and call default function
    args = parser.parse_args()
    args.func(args)
