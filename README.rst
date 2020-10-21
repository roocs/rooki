rooki
=====

.. image:: https://readthedocs.org/projects/rooki/badge/?version=latest
    :target: https://rooki.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.com/roocs/rooki.svg?branch=master
    :target: https://travis-ci.com/roocs/rooki
    :alt: Build Status

.. image:: https://img.shields.io/github/license/roocs/rooki.svg
    :target: https://github.com/roocs/rooki/blob/master/LICENSE
    :alt: GitHub license


Rooki is a client for roocs climate data operations service (rook_).

The rooki python package is a lightweight wrapper around the birdy_ client library for WPS.
It provides the *rooki* python object that has methods that can be called to query and invoke
the rook_ WPS.

A Jupyter Notebook is provided to demonstrate the basic use of rooki.


* Free software: BSD - see LICENSE file in top-level package directory


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


Usage
-----

.. code-block:: python

  # Optional: set ROOK_URL ... or use default
  import os
  os.environ['ROOK_URL'] = http://localhost:5000/wps
  # import rooki
  from rooki import rooki
  # run subset on c3s-cmip5 dataset with time selection
  response = rooki.subset(
    collection='c3s-cmip5.output1.ICHEC.EC-EARTH.historical.day.atmos.day.r1i1p1.tas.latest',
    time='1860-01-01/1900-12-30')
  # successful?
  response.ok
  # show links to result files
  response.download_urls()

Credits
-------

This package was created with Cookiecutter_ and the `cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _birdy: https://github.com/bird-house/birdy
.. _rook: https://github.com/roocs/rook
