from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='socialschools-cms',
    version=version,
    description='socialschools plugin for django-cms',
    author='Pratik Vyas',
    author_email='pratik.vyas@changer.nl',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
)