import unittest

from model.graph import Graph
from production.p1 import p1
from graphs.graphs_p1 import complex_graph_with_match, graph_with_no_match, graph_with_incorrect_hyper_edge_label, \
    graph_with_incorrect_hyper_edge_attribute, graph_with_incorrect_hyper_edge_node_attribute
from graphs.common import left_side_of_p1, left_side_of_p2


class TestP1(unittest.TestCase):

    def test_for_left_side_of_p1(self):
        expected_nodes_size = 9
        expected_edges_size = 12
        expected_hyper_edges_size = 4

        graph = left_side_of_p1()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)

    def test_for_complex_graph_with_match(self):
        expected_nodes_size = 11
        expected_edges_size = 16
        expected_hyper_edges_size = 4

        graph = complex_graph_with_match()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)

    def test_for_graph_with_no_match(self):
        expected_nodes_size = 4
        expected_edges_size = 3
        expected_hyper_edges_size = 1

        graph = graph_with_no_match()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)

    def test_for_empty_graph(self):
        expected_nodes_size = 0
        expected_edges_size = 0
        expected_hyper_edges_size = 0

        graph = Graph()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)

    def test_for_left_side_of_p2(self):
        expected_nodes_size = 5
        expected_edges_size = 5
        expected_hyper_edges_size = 1

        graph = left_side_of_p2()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)

    def test_for_graph_with_incorrect_hyper_edge_node_attribute(self):
        expected_nodes_size = 4
        expected_edges_size = 4
        expected_hyper_edges_size = 1

        graph = graph_with_incorrect_hyper_edge_node_attribute()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)

    def test_for_graph_with_incorrect_hyper_edge_attribute(self):
        expected_nodes_size = 4
        expected_edges_size = 4
        expected_hyper_edges_size = 1

        graph = graph_with_incorrect_hyper_edge_attribute()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)

    def test_for_graph_with_incorrect_hyper_edge_label(self):
        expected_nodes_size = 4
        expected_edges_size = 4
        expected_hyper_edges_size = 1

        graph = graph_with_incorrect_hyper_edge_label()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
