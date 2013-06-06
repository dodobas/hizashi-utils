from distutils.core import setup

setup(
    name='hizashi-utils',
    version='0.1.0',
    author='Dražen Odobašić',
    author_email='dodobasic@gmail.com',
    packages=['hizashi-utils'],
    scripts=['hizashi-utils/bin/hizashi.py'],
    url='',
    license='LICENSE.txt',
    description='Utils for managing Hizashi Django environment',
    install_requires=[
        "Django >= 1.5"
    ]
)
