# rooki

[![Build Status](https://travis-ci.com/roocs/rooki.svg?branch=master)](https://travis-ci.com/roocs/rooki)

A client for roocs climate data operations service.


* Free software: BSD - see LICENSE file in top-level package directory


## NBViewer

https://nbviewer.jupyter.org/github/roocs/rooki/tree/master/notebooks/


## Features

* TODO

## Installation

```
$ conda create -n rooki python=3.8
$ conda activate rooki
$ pip install git+https://github.com/roocs/rooki@master#egg=rooki
```

## Usage

```
from rooki import rooki
result = rooki.subset()
result.download_urls()
```

# Credits

This package was created with `Cookiecutter` and the `audreyr/cookiecutter-pypackage` project template.

 * Cookiecutter: https://github.com/audreyr/cookiecutter
 * cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
