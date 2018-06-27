# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pgpipelines',
    version='0.0.1',
    description='# Pgpipeline: postgres pipeline for Scrapy',
    long_description=open('README.md').read(),
    author='kota999',
    author_email='kota99949@gmail.com',
    url='https://github.com/kota999/pgpipelines',
    license=open('LICENSE').read(),
    install_requires=['psycopg2', 'sqlalchemy', 'dataset'],
    packages=find_packages()
)
