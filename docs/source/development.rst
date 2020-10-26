.. _dev_guide:

Development Guide
=================

Get Started!
------------

Check out code from the rooki GitHub repo and start the installation:

.. code-block:: console

   $ git clone https://github.com/roocs/rooki.git
   $ cd rooki
   $ conda env create -f environment.yml
   $ conda activate rooki
   $ pip install -e .

Install additional dependencies:

.. code-block:: console

  $ pip install -r requirements_dev.txt

When you're done making changes, check that your changes pass `black`, `flake8` and the tests:

.. code-block:: console

    $ black rooki tests
    $ flake8 rooki tests
    $ pytest tests

Or use the Makefile:

.. code-block:: console

     $ make lint
     $ make test


Add pre-commit hooks
--------------------

Before committing your changes, we ask that you install `pre-commit` in your environment.
`Pre-commit` runs git hooks that ensure that your code resembles that of the project
and catches and corrects any small errors or inconsistencies when you `git commit`:

.. code-block:: console

     $ conda install -c conda-forge pre_commit
     $ pre-commit install

Write Documentation
-------------------

You can find the documentation in the `docs/source` folder. To generate the Sphinx
documentation locally you can use the `Makefile`:

.. code-block:: console

  $ make docs

Bump a new version
------------------

Make a new version of rooki in the following steps:

* Make sure everything is commit to GitHub.
* Update ``HISTORY.rst`` with the next version.
* Dry Run: ``bumpversion --dry-run --verbose patch  # --new-version 0.2.1``
* Do it: ``bumpversion --new-version patch``
* ... or: ``bumpversion --new-version minor  # --new-version 0.3.0``
* Push it: ``git push --tags``

See the bumpversion_ documentation for details.

.. _bumpversion: https://pypi.org/project/bumpversion/
