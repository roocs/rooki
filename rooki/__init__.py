# -*- coding: utf-8 -*-

"""Top-level package for rooki."""

from rooki.client import Rooki

# from rooki import operators


rooki = Rooki()


def reinit():
    global rooki
    rooki = Rooki()


__all__ = [
    "rooki",
    "Rooki",
    "reinit",
    # "operators",
]
