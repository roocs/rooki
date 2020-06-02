
"""A mock-up rooki API."""

import json
from collections import defaultdict

from rooki import rooki


class Operator:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _tree(self, tree=defaultdict(dict)):
        args = [arg._tree(tree) for arg in self.args]
        tree['steps'][self.method_key] = {
            'run': self.METHOD,
            'in': {
                'data_ref': _unpack_if_single([arg.data_ref for arg in self.args]),
                **self.kwargs,
            }
        }
        tree['outputs']['output'] = self.data_ref
        return tree

    def _serialise(self, doc='tree workflow'):
        tree = self._tree()
        tree['doc'] = doc
        return json.dumps(tree)

    def orchestrate(self):
        return rooki.orchestrate(workflow=self._serialise(), mode='tree')

    @property
    def method_key(self):
        methods = self._get_methods([])
        return f'{self.METHOD}_{self.variable}_{methods.count(self.METHOD)}'

    def _get_methods(self, methods):
        method_names = [arg._get_methods(methods) for arg in self.args]
        methods.append(self.METHOD)
        return methods

    @property
    def data_ref(self):
        return f'{self.method_key}/output'

    @property
    def variable(self):
        return _unpack_if_single([arg.variable for arg in self.args])


class Input:

    def __init__(self, variable, dataset):
        self.variable = variable
        self.dataset = dataset

    def _tree(self, tree=defaultdict(dict)):
        tree['inputs'][self.variable] = self.dataset
        return tree

    def _get_methods(self, methods):
        return methods

    @property
    def data_ref(self):
        return f'inputs/{self.variable}'


class Average(Operator):
    METHOD = 'average'


class Subset(Operator):
    METHOD = 'subset'


def _unpack_if_single(list):
    try:
        [item] = list
    except ValueError:
        item = list
    return item
