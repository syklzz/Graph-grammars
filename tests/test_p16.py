import unittest

from graphs.graphs_p16 import left_side_of_p16, complex_graph_with_match_p16, complex_graph_with_no_match_p16, \
    graph_with_incorrect_hyper_edge_attribute, graph_with_incorrect_hyper_label_attribute
from model.graph import Graph
from production.p16 import p16
from production.p4 import p4
from production.p8 import p8


class TestP16(unittest.TestCase):

    def test_for_left_side_of_p16(self):
        expected_nodes_size = 5
        expected_edges_size = 0
        expected_hyper_edges_size = 1
        expected_r1 = 1

        graph = left_side_of_p16()
        graph.draw_graph()
        p16(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)

    def test_for_complex_graph_with_match(self):
        expected_nodes_size = 9
        expected_edges_size = 7
        expected_hyper_edges_size = 2
        expected_r1 = 1
        expected_r2 = 0

        graph = complex_graph_with_match_p16()
        graph.draw_graph()
        p16(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
        self.assertTrue(graph.hyper_edges[1].r == expected_r2)

    def test_for_graph_with_no_match(self):
        expected_nodes_size = 9
        expected_edges_size = 7
        expected_hyper_edges_size = 2
        expected_r1 = 0
        expected_r2 = 0

        graph = complex_graph_with_no_match_p16()
        graph.draw_graph()
        p16(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
        self.assertTrue(graph.hyper_edges[1].r == expected_r2)

    def test_for_empty_graph(self):
        expected_nodes_size = 0
        expected_edges_size = 0
        expected_hyper_edges_size = 0

        graph = Graph()
        graph.draw_graph()
        p16(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)

    def test_for_graph_with_incorrect_hyper_edge_attribute(self):
        expected_nodes_size = 5
        expected_edges_size = 0
        expected_hyper_edges_size = 1
        expected_r1 = 1

        graph = graph_with_incorrect_hyper_edge_attribute()
        graph.draw_graph()
        p16(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)


    def test_for_graph_with_incorrect_hyper_edge_label(self):
        expected_nodes_size = 5
        expected_edges_size = 0
        expected_hyper_edges_size = 1
        expected_r1 = 0

        graph = graph_with_incorrect_hyper_label_attribute()
        graph.draw_graph()
        p16(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
