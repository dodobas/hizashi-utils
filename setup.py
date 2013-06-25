# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='hizashi-utils',
    version='0.3.2',
    author='Dražen Odobašić',
    author_email='dodobasic@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    scripts=['hizashi_utils/bin/hizashi.py'],
    url='https://github.com/dodobas/hizashi-utils',
    keywords='django hizashi utils helpers',
    license='LICENSE.txt',
    description='Utils for managing Django Hizashi environment',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ],
    setup_requires=[
        "setuptools_git >= 0.3"
    ],
    install_requires=[
        "Django >= 1.5"
    ]
)
