# rooki

[![Build Status](https://travis-ci.com/roocs/rooki.svg?branch=master)](https://travis-ci.com/roocs/rooki)

A client for roocs climate data operations service.


* Free software: BSD - see LICENSE file in top-level package directory


## Online Demo

You can try Rooki online using Binder (just click on the binder link below),
or view the notebooks on NBViewer.

[![Binder Launcher](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/roocs/rooki.git/master?filepath=notebooks)
[![NBViewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/roocs/rooki/tree/master/notebooks/)


## Features

* TODO

## Installation

```bash
$ conda create -n rooki -c conda-forge python=3.8 birdy
$ conda activate rooki
$ pip install git+https://github.com/roocs/rooki@master#egg=rooki
```

## Usage

```python
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
```

# Credits

This package was created with `Cookiecutter` and the `audreyr/cookiecutter-pypackage` project template.

 * Cookiecutter: https://github.com/audreyr/cookiecutter
 * cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
