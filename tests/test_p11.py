import unittest

from graphs import graphs_p11
from graphs.common import empty_graph
from production.p11 import p11

class TestP11(unittest.TestCase):
    def test_left_side_matching(self):
        expected_nodes_size = 11
        expected_edges_size = 15
        expected_hyper_edges_size = 5
        
        graph = graphs_p11.exact_left_side()
        graph.draw_graph()
        p11(graph)
        graph.draw_graph()
        
        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        
    def test_for_complex_graph_with_match(self):
        expected_nodes_size = 11 + 2
        expected_edges_size = 15 + 3
        expected_hyper_edges_size = 5 + 1
        
        graph = graphs_p11.complex_graph_with_match()
        graph.draw_graph()
        p11(graph)
        graph.draw_graph()
        
        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        
    def test_for_graph_with_no_match(self):
        expected_nodes_size = 8
        expected_edges_size = 9
        expected_hyper_edges_size = 2
        
        graph = graphs_p11.graph_with_no_match()
        graph.draw_graph()
        p11(graph)
        graph.draw_graph()
        
        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        
    def test_for_empty_graph(self):
        expected_nodes_size = 0
        expected_edges_size = 0
        expected_hyper_edges_size = 0
        
        graph = empty_graph()
        graph.draw_graph()
        p11(graph)
        graph.draw_graph()
        
        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
       
       
    def test_for_graph_wrong_label(self):
        expected_nodes_size = 7
        expected_edges_size = 7
        expected_hyper_edges_size = 1
        
        graph = graphs_p11.graph_wrong_label()
        graph.draw_graph()
        p11(graph)
        graph.draw_graph()
        
        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
           
     
    def test_for_graph_wrong_hanging_node(self):
        expected_nodes_size = 7
        expected_edges_size = 7
        expected_hyper_edges_size = 1
        
        graph = graphs_p11.graph_wrong_hanging_node()
        graph.draw_graph()
        p11(graph)
        graph.draw_graph()
        
        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        
        
    def test_for_graph_with_wrong_r(self):
        expected_nodes_size = 7
        expected_edges_size = 7
        expected_hyper_edges_size = 1
        
        graph = graphs_p11.graph_wrong_r()
        graph.draw_graph()
        p11(graph)
        graph.draw_graph()
        
        self.assertTrue(len(graph.nodes) == expected_nodes_size)
        self.assertTrue(len(graph.edges) == expected_edges_size)
        self.assertTrue(len(graph.hyper_edges) == expected_hyper_edges_size)
        