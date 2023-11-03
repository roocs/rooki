rooki
=====

|pypi| |conda| |build| |black|


Rooki is a client for roocs_ climate data operations service (rook_).

The rooki python package is a lightweight wrapper around the birdy_ client library for WPS.
It provides the *rooki* python object that has methods that can be called to query and invoke
the rook_ WPS.

A Jupyter Notebook is provided to demonstrate the basic use of rooki.


Online Demo
-----------

You can try Rooki online using Binder (just click on the binder link below),
or view the notebooks on NBViewer.

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/roocs/rooki.git/master?filepath=notebooks
   :alt: Binder Launcher

.. image:: https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg
   :target: https://nbviewer.jupyter.org/github/roocs/rooki/tree/master/notebooks/
   :alt: NBViewer
   :height: 20

Credits
-------

This package was created with Cookiecutter_ and the `cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _birdy: https://github.com/bird-house/birdy
.. _roocs: https://github.com/roocs
.. _rook: https://github.com/roocs/rook
.. _documentation: https://rooki.readthedocs.io/en/latest/

.. |pypi| image:: https://img.shields.io/pypi/v/rooki.svg
   :target: https://pypi.python.org/pypi/rooki
   :alt: PyPI

.. |conda| image:: https://img.shields.io/conda/vn/conda-forge/rooki.svg
   :target: https://anaconda.org/conda-forge/rooki
   :alt: Conda Forge

.. |build| image:: https://github.com/roocs/rooki/workflows/build/badge.svg
   :target: https://github.com/roocs/rooki/actions
   :alt: Build Status

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/python/black
   :alt: Black
