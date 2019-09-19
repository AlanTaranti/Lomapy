# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from lomapy.recursos.sdk import sdk

__description__ = 'Lomapy'
__long_description__ = 'Biblioteca Python para API do Lomadee'

__author__ = 'Alan Taranti'
__author_email__ = 'alan.taranti@gmail.com'


testing_extras = [
    'pytest',
    'pytest-cov',
    "python-dotenv"
]

setup(
    name='lomapy',
    version=sdk.VERSAO,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/AlanTaranti/Lomapy',
    keywords='lomapy, lomadee',
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)
