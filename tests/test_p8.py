import unittest

from model.graph import Graph
from production.p8 import p8
from graphs.graphs_p8 import complex_graph_with_match, graph_with_no_match, graph_with_incorrect_hyper_edge_attribute, \
    graph_with_incorrect_hanging_node_attribute, left_side_of_p8, mod_left_side_of_p8


class TestP8(unittest.TestCase):

    def test_for_left_side_of_p8(self):
        expected_nodes_size = 7
        expected_edges_size = 2
        expected_hyper_edges_size = 2
        expected_r1 = 1
        expected_r2 = 1

        graph = left_side_of_p8()
        graph.draw_graph()
        p8(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
        self.assertTrue(graph.hyper_edges[1].r == expected_r2)

    def test_for_mod_left_side_of_p8(self):
        expected_nodes_size = 7
        expected_edges_size = 2
        expected_hyper_edges_size = 2
        expected_r1 = 1
        expected_r2 = 1

        graph = mod_left_side_of_p8()
        graph.draw_graph()
        p8(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
        self.assertTrue(graph.hyper_edges[1].r == expected_r2)

    def test_for_complex_graph_with_match(self):
        expected_nodes_size = 8
        expected_edges_size = 9
        expected_hyper_edges_size = 2
        expected_r1 = 1
        expected_r2 = 1

        graph = complex_graph_with_match()
        graph.draw_graph()
        p8(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
        self.assertTrue(graph.hyper_edges[1].r == expected_r2)

    def test_for_graph_with_no_match(self):
        expected_nodes_size = 3
        expected_edges_size = 2
        expected_hyper_edges_size = 1
        expected_r = 1

        graph = graph_with_no_match()
        graph.draw_graph()
        p8(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r)

    def test_for_empty_graph(self):
        expected_nodes_size = 0
        expected_edges_size = 0
        expected_hyper_edges_size = 0

        graph = Graph()
        graph.draw_graph()
        p8(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)

    def test_for_graph_with_incorrect_hanging_node_attribute(self):
        expected_nodes_size = 7
        expected_edges_size = 2
        expected_hyper_edges_size = 2
        expected_r1 = 0
        expected_r2 = 1

        graph = graph_with_incorrect_hanging_node_attribute()
        graph.draw_graph()
        p8(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
        self.assertTrue(graph.hyper_edges[1].r == expected_r2)

    def test_for_graph_with_incorrect_hyper_edge_attribute(self):
        expected_nodes_size = 7
        expected_edges_size = 2
        expected_hyper_edges_size = 2
        expected_r1 = 0
        expected_r2 = 1

        graph = graph_with_incorrect_hyper_edge_attribute()
        graph.draw_graph()
        p8(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
        self.assertTrue(graph.hyper_edges[1].r == expected_r2)
