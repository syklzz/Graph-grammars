import unittest

import graphs.graphs_p17 as graphs
from model.graph import Graph
from production.p17 import p17


class TestP17(unittest.TestCase):
    def test_exact_math(self):
        left = graphs.exact_match()
        right = graphs.exact_match_production()

        p17(left)

        self.assertTrue(left == right)

    def test_for_complex_graph_with_match(self):
        left = graphs.complex_graph_with_match()
        right = graphs.complex_graph_with_match_production()

        p17(left)

        self.assertTrue(left == right)

    def test_for_graph_with_no_match(self):
        left = graphs.graph_with_no_match()
        right = graphs.graph_with_no_match()

        p17(left)
        self.assertTrue(left == right)

    def test_for_empty_graph(self):
        left = Graph()
        right = Graph()

        p17(left)
        self.assertTrue(left == right)

    def test_for_graph_with_incorrect_hyper_edge_attribute(self):
        left = graphs.graph_with_incorrect_hyper_edge_attribute()
        right = graphs.graph_with_incorrect_hyper_edge_attribute()

        p17(left)

        self.assertTrue(left == right)

    def test_for_graph_with_incorrect_hanging_node_attribute(self):
        left = graphs.graph_with_incorrect_hanging_node_attribute()
        right = graphs.graph_with_incorrect_hanging_node_attribute()

        p17(left)

        self.assertTrue(left == right)

    def test_for_graph_with_incorrect_accompanying_edge_value(self):
        left = graphs.graph_with_incorrect_accompanying_edge_value()
        right = graphs.graph_with_incorrect_accompanying_edge_value()

        p17(left)

        self.assertTrue(left == right)
