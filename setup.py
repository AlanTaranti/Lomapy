# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from lomapy.recursos.sdk import sdk

descricao = 'Lomapy'

with open("README.md") as f:
    descricao_longa = f.read()

autor = 'Alan Taranti'
autor_email = 'alan.taranti@gmail.com'


testing_extras = [
    'pytest',
    'pytest-cov',
    "python-dotenv"
]

setup(
    name='lomapy',
    version=sdk.VERSAO,
    author=autor,
    author_email=autor_email,
    packages=find_packages(),
    license='MIT',
    description=descricao,
    long_description=descricao_longa,
    long_description_content_type='text/markdown',
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
