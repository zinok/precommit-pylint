""" Setup script for Precommit Pylint """

from setuptools import find_packages
from setuptools import setup

setup(
    name='precommit-pylint',
    version='0.1.0',
    description='Pre-commit hook that runs pylint and allows to configure score limit',
    author='Andrii Zinchenko',
    author_email='mail@zinok.org',
    url='http://www.zinok.org',
    keywords="git commit pre-commit hook pylint python",
    platforms=['Any'],
    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'pylint',
        'future'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    entry_points={
        'console_scripts': [
            'precommit-pylint = precommit_pylint.main:main',
        ]
    }
)
