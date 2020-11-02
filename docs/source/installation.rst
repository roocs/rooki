.. _installation:

Installation
============

Install from Anaconda
---------------------

* TODO

Install from PyPi
-----------------

Create a conda environment with birdy and install with pip:

.. code-block:: console

  $ conda create -n rooki -c conda-forge python=3.8 birdy
  $ conda activate rooki
  $ pip install rooki


Install from GitHub
-------------------

Check out code from the rooki GitHub repo and start the installation:

.. code-block:: console

   $ git clone https://github.com/roocs/rooki.git
   $ cd rooki
   $ conda env create -f environment.yml
   $ pip install -e .
