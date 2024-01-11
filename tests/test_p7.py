import unittest

from graphs import graphs_p7
from graphs.common import empty_graph
from production.p7 import p7

class TestP7(unittest.TestCase):
    def test_left_side_matching(self):
        expected_nodes_size = 4
        expected_edges_size = 0
        expected_hyper_edges_size = 1
        expected_r1 = 1

        graph = graphs_p7.exact_left_side()
        graph.draw_graph()
        p7(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)


    def test_for_complex_graph_with_match(self):
        expected_nodes_size = 7
        expected_edges_size = 8
        expected_hyper_edges_size = 2
        expected_r1 = 1
        expected_r2 = 0

        graph = graphs_p7.complex_graph_with_match()
        graph.draw_graph()
        p7(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)
        self.assertTrue(graph.hyper_edges[1].r == expected_r2)


    def test_for_graph_with_no_match(self):
        expected_nodes_size = 6
        expected_edges_size = 6
        expected_hyper_edges_size = 1
        expected_r1 = 0

        graph = graphs_p7.graph_with_no_match()
        graph.draw_graph()
        p7(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)


    def test_for_empty_graph(self):
        expected_nodes_size = 0
        expected_edges_size = 0
        expected_hyper_edges_size = 0

        graph = empty_graph()
        graph.draw_graph()
        p7(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)


    def test_for_graph_with_incorrect_hyper_edge_attribute(self):
        expected_nodes_size = 4
        expected_edges_size = 0
        expected_hyper_edges_size = 1
        expected_r1 = 1

        graph = graphs_p7.graph_wrong_r()
        graph.draw_graph()
        p7(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)


    def test_for_graph_with_incorrect_hyper_edge_label(self):
        expected_nodes_size = 4
        expected_edges_size = 0
        expected_hyper_edges_size = 1
        expected_r1 = 0

        graph = graphs_p7.graph_wrong_label()
        graph.draw_graph()
        p7(graph)
        graph.draw_graph()

        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        self.assertTrue(graph.hyper_edges[0].r == expected_r1)