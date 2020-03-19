# -*- coding: utf-8 -*-

"""Console script for rooki."""

__author__ = """Carsten Ehbrecht"""
__contact__ = "ehbrecht@dkrz.de"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"

import sys
import click


@click.command()
def main(args=None):
    """Console script for rooki."""
    click.echo("Replace this message by putting your code into "
               "rooki.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
