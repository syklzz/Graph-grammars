import unittest

from graphs.graphs_p4 import left_side_of_p4, complex_graph_with_match_p4, complex_graph_with_no_match_p4, \
    graph_with_incorrect_hanging_node_attributes, graph_with_incorrect_hyper_edge_attribute, \
    graph_with_incorrect_hyper_label_attribute
from model.graph import Graph
from production.p4 import p4
from production.p8 import p8


class TestP4(unittest.TestCase):

    def test_for_left_side_of_p4(self):
        expected_nodes_size = 9
        expected_edges_size = 12
        expected_hyper_edges_size = 4
        expected_r1 = 0
        expected_r2 = 0
        expected_r3 = 0
        expected_r4 = 0

        graph = left_side_of_p4()
        graph.draw_graph()
        p4(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
        self.assertTrue(graph.hyper_edges[1].r == expected_r2)
        self.assertTrue(graph.hyper_edges[2].r == expected_r3)
        self.assertTrue(graph.hyper_edges[3].r == expected_r4)

    def test_for_complex_graph_with_match(self):
        expected_nodes_size = 11
        expected_edges_size = 15
        expected_hyper_edges_size = 4
        expected_r1 = 0
        expected_r2 = 0
        expected_r3 = 0
        expected_r4 = 0

        graph = complex_graph_with_match_p4()
        graph.draw_graph()
        p4(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
        self.assertTrue(graph.hyper_edges[1].r == expected_r2)
        self.assertTrue(graph.hyper_edges[2].r == expected_r3)
        self.assertTrue(graph.hyper_edges[3].r == expected_r4)

    def test_for_graph_with_no_match(self):
        graph = complex_graph_with_no_match_p4()

        expected_nodes_size = len(graph.nodes)
        expected_edges_size = len(graph.edges)
        expected_hyper_edges_size = len(graph.hyper_edges)

        graph.draw_graph()
        p8(graph)
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
        p4(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)

    def test_for_graph_with_incorrect_hanging_node_attribute(self):
        expected_nodes_size = 6
        expected_edges_size = 6
        expected_hyper_edges_size = 1
        expected_r1 = 1

        graph = graph_with_incorrect_hanging_node_attributes()
        graph.draw_graph()
        p4(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)

    def test_for_graph_with_incorrect_hyper_edge_attribute(self):
        expected_nodes_size = 6
        expected_edges_size = 6
        expected_hyper_edges_size = 1
        expected_r1 = 0

        graph = graph_with_incorrect_hyper_edge_attribute()
        graph.draw_graph()
        p4(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)

    def test_for_graph_with_incorrect_hyper_edge_label(self):
        expected_nodes_size = 6
        expected_edges_size = 6
        expected_hyper_edges_size = 1
        expected_r1 = 1

        graph = graph_with_incorrect_hyper_label_attribute()
        graph.draw_graph()
        p4(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
