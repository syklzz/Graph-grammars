import unittest

from model.graph import Graph
from production.p2 import p2


def prepare_graph():
    return Graph()


def expected_graph():
    return Graph()


class TestP2(unittest.TestCase):

    def test_production(self):
        graph = prepare_graph()
        p2(graph)
        self.assertTrue(graph.equals(expected_graph()))
