import os
from setuptools import find_packages, setup


def read(fpath):
    """Reads a file within package directories"""
    with open(os.path.join(os.path.dirname(__file__), fpath)) as f:
        return f.read()


setup(
    name='django-authentication-app',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Provides authentication forms to register and login into the system',
    long_description=read('README.md'),
    url='http://www.codingwithalex.com',
    author='Alex Silva',
    author_email='alex@codingwithalex.com',
    python_requires='>=3',
    zip_safe=False,
    install_requires=[
        'django==4.1.4',
        'django-allauth==0.51.0'
    ],
    dependency_links=[
        'git+ssh://git@github.com/alesima/django-base-app.git#egg=django-base-app'
    ]
)
