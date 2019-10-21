# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# Metadados
metadados = {}
exec(compile(open("lomapy/metadados.py").read(), "lomapy/metadados.py", 'exec'), metadados)

# Descrições
descricao = 'Lomapy'

with open("README.md") as f:
    descricao_longa = f.read()

# Requisitos
with open('requirements.txt') as f:
    install_requires = f.readlines()

with open('requirements-dev.txt') as f:
    tests_require = f.readlines()

# Classificadores
classificadores = [
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Operating System :: OS Independent',
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
    "Topic :: Utilities",
    'Environment :: Web Environment',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License',
]

setup(
    name='lomapy',
    version=metadados['__version__'],
    author=metadados['__author__'],
    author_email=metadados['__email__'],
    packages=find_packages(),
    license=metadados['__license__'],
    description=descricao,
    long_description=descricao_longa,
    long_description_content_type='text/markdown',
    url='https://github.com/AlanTaranti/Lomapy',
    keywords='lomapy, lomadee, product advertising, api',
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    classifiers=classificadores,
    tests_require=tests_require,
)
