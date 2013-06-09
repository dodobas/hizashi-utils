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

if __name__ == "__main__":
    # parse the args, and call default function
    args = parser.parse_args()
    args.func(args)
