# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='hizashi-utils',
    version='0.1.0',
    author='Dražen Odobašić',
    author_email='dodobasic@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    scripts=['hizashi-utils/bin/hizashi.py'],
    url='https://github.com/dodobas/hizashi-utils',
    license='LICENSE.txt',
    description='Utils for managing Hizashi Django environment',
    setup_requires=[
        "setuptools_git >= 0.3"
    ],
    install_requires=[
        "Django >= 1.5"
    ]
)
