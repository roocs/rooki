"""A mock-up rooki API."""

import json
from collections import defaultdict

from .client import rooki


class Operator:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _tree(self, tree=defaultdict(dict)):
        # args = [arg._tree(tree) for arg in self.args]
        [arg._tree(tree) for arg in self.args]
        tree["steps"][self.method_key] = {
            "run": self.METHOD,
            "in": {
                "collection": _unpack_if_single([arg.collection for arg in self.args]),
                **self.kwargs,
            },
        }
        tree["outputs"]["output"] = self.collection
        return tree

    def _serialise(self, doc="workflow"):
        tree = self._tree()
        tree["doc"] = doc
        return json.dumps(tree)

    def orchestrate(self):
        return rooki.orchestrate(workflow=self._serialise())

    @property
    def method_key(self):
        methods = self._get_methods([])
        return f"{self.METHOD}_{self.variable}_{methods.count(self.METHOD)}"

    def _get_methods(self, methods):
        # method_names = [arg._get_methods(methods) for arg in self.args]
        [arg._get_methods(methods) for arg in self.args]
        methods.append(self.METHOD)
        return methods

    @property
    def collection(self):
        return f"{self.method_key}/output"

    @property
    def variable(self):
        return _unpack_if_single([arg.variable for arg in self.args])


class Input:
    def __init__(self, variable, dataset):
        self.variable = variable
        self.dataset = dataset

    def _serialise(self, doc="workflow"):
        tree = self._tree()
        tree["doc"] = doc
        return json.dumps(tree)

    def orchestrate(self):
        return rooki.orchestrate(workflow=self._serialise())

    def _tree(self, tree=defaultdict(dict)):
        tree["inputs"][self.variable] = self.dataset
        return tree

    def _get_methods(self, methods):
        return methods

    @property
    def collection(self):
        return f"inputs/{self.variable}"


class Average(Operator):
    METHOD = "average"


class Subset(Operator):
    METHOD = "subset"


class Diff(Operator):
    METHOD = "diff"

    def _tree(self, tree=defaultdict(dict)):
        # args = [arg._tree(tree) for arg in self.args]
        [arg._tree(tree) for arg in self.args]
        tree["steps"][self.method_key] = {
            "run": self.METHOD,
            "in": {
                "collection_a": _unpack_if_single([self.args[0].collection]),
                "collection_b": _unpack_if_single([self.args[1].collection]),
                **self.kwargs,
            },
        }
        tree["outputs"]["output"] = self.collection
        return tree

    @property
    def variable(self):
        return "var"


def _unpack_if_single(list):
    try:
        [item] = list
    except ValueError:
        item = list
    return item
