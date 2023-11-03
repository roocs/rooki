#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

__author__ = "Carsten Ehbrecht"
__contact__ = "ehbrecht@dkrz.de"
__copyright__ = "Copyright 2023 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__version__ = "0.6.0"

# One strategy for storing the overall version is to put it in the top-level
# package's __init__ but Nb. __init__.py files are not needed to declare
# packages in Python 3
# from rooki import __version__ as _package_version

# Populate long description setting with content of README
#
# Use markdown format read me file as GitHub will render it automatically
# on package page
with open("README.rst") as readme_file:
    _long_description = readme_file.read()


requirements = [line.strip() for line in open("requirements.txt")]
test_requirements = [
    "pytest",
]


setup(
    author=__author__,
    author_email=__contact__,
    # See:
    # https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="A client for roocs climate data operations service.",
    license=__license__,
    # This qualifier can be used to selectively exclude Python versions
    python_requires=">=3.9.0",
    install_requires=[
        requirements,
    ],
    long_description=_long_description,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="rooki",
    name="rooki",
    packages=find_packages(include=["rooki"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/roocs/rooki",
    version=__version__,
    zip_safe=False,
)
