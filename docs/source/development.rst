.. highlight:: shell

Development
***********

Get Started!
============

Check out code from the rooki GitHub repo and start the installation::

   $ git clone https://github.com/bird-house/birdy.git
   $ cd rooki https://github.com/roocs/rooki.git
   $ conda env create -f environment.yml
   $ python setup.py develop

Install additional dependencies::

  $ pip install -r requirements_dev.txt

When you're done making changes, check that your changes pass `flake8` and the tests::

    $ flake8
    $ pytest

   Or use the Makefile::

     $ make lint
     $ make test

Write Documentation
===================

You can find the documentation in the `docs/source` folder. To generate the Sphinx
documentation locally you can use the `Makefile`::

  $ make docs

Bump a new version
===================

Make a new version of rooki in the following steps:

* Make sure everything is commit to GitHub.
* Update ``HISTORY.rst`` with the next version.
* Dry Run: ``bumpversion --dry-run --verbose patch  # --new-version 0.2.1``
* Do it: ``bumpversion --new-version patch``
* ... or: ``bumpversion --new-version minor  # --new-version 0.3.0``
* Push it: ``git push --tags``

See the bumpversion_ documentation for details.

.. _bumpversion: https://pypi.org/project/bumpversion/
