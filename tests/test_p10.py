import unittest

from graphs.graphs_p10 import *
from production.p10 import p10


class TestP10(unittest.TestCase):
    @staticmethod
    def _build_valid_graph() -> Graph:
        graph = Graph()

        node1 = Node(0, 0, 0)
        node2 = Node(2, 0, 0)
        node3 = Node(2, 2, 0)
        node4 = Node(0, 2, 0)
        node5 = Node(3, 1, 0)
        node6 = Node(1, 0, 1)  # hanging node
        graph.add_nodes([node1, node2, node3, node4, node5, node6])

        graph.add_edge(Edge(node1, node6, 1))
        graph.add_edge(Edge(node6, node2, 1))
        graph.add_edge(Edge(node2, node5, 1))
        graph.add_edge(Edge(node5, node3, 1))
        graph.add_edge(Edge(node3, node4, 1))
        graph.add_edge(Edge(node4, node1, 1))

        graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4, node5], 0, Label.P))

        return graph

    @staticmethod
    def _build_complex_valid_graph() -> Graph:
        graph = Graph()

        # Matching graph
        node1 = Node(0, 0, 0)
        node2 = Node(2, 0, 0)
        node3 = Node(2, 2, 0)
        node4 = Node(0, 2, 0)
        node5 = Node(3, 1, 0)
        node6 = Node(1, 0, 1)  # hanging node

        graph.add_edge(Edge(node1, node6, 1))
        graph.add_edge(Edge(node6, node2, 1))
        graph.add_edge(Edge(node2, node5, 1))
        graph.add_edge(Edge(node5, node3, 1))
        graph.add_edge(Edge(node3, node4, 1))
        graph.add_edge(Edge(node4, node1, 1))

        # Additional nodes and edges
        node7 = Node(1, 4, 0)
        node8 = Node(3, 3, 0)

        graph.add_edge(Edge(node4, node7, 1))
        graph.add_edge(Edge(node7, node3, 1))
        graph.add_edge(Edge(node7, node8, 1))
        graph.add_edge(Edge(node8, node3, 1))
        graph.add_edge(Edge(node8, node5, 1))

        graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8])
        graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4, node5], 0, Label.P))

        return graph

    @staticmethod
    def _build_invalid_graph() -> Graph:
        graph = Graph()

        node1 = Node(0, 0, 0)
        node2 = Node(0, 2, 0)
        node3 = Node(2, 2, 0)
        node4 = Node(2.5, 1, 0)
        node5 = Node(2, 0, 1)
        graph.add_nodes([node1, node2, node3, node4, node5])

        graph.add_edge(Edge(node1, node2, 0))
        graph.add_edge(Edge(node2, node3, 0))
        graph.add_edge(Edge(node3, node4, 0))
        graph.add_edge(Edge(node4, node5, 0))
        graph.add_edge(Edge(node5, node1, 0))

        graph.add_hyper_edge(
            HyperEdge([node1, node2, node3, node4, node5], r=1, label=Label.Q)
        )

        return graph

    @staticmethod
    def _build_incomplete_graph() -> Graph:
        graph = Graph()

        node1 = Node(0, 0, 0)
        node2 = Node(0, 2, 0)
        node3 = Node(2, 2, 0)
        graph.add_nodes([node1, node2, node3])

        graph.add_edge(Edge(node1, node2, 0))
        graph.add_edge(Edge(node2, node3, 0))
        graph.add_edge(Edge(node1, node3, 0))

        graph.add_hyper_edge(HyperEdge([node1, node2, node3], r=1, label=Label.P))

        return graph

    def test_valid_graph(self):
        expected_nodes_size = 13
        expected_edges_size = 20
        expected_hyper_edges_size = 5

        graph = self._build_complex_valid_graph()
        graph.draw_graph()
        p10(graph)
        graph.draw_graph()

        self.assertEqual(len(graph.nodes), expected_nodes_size)
        self.assertEqual(len(graph.edges), expected_edges_size)
        self.assertEqual(len(graph.hyper_edges), expected_hyper_edges_size)

    def test_complex_valid_graph(self):
        expected_nodes_size = 13
        expected_edges_size = 20
        expected_hyper_edges_size = 5

        graph = self._build_complex_valid_graph()
        graph.draw_graph()
        p10(graph)
        graph.draw_graph()

        self.assertEqual(len(graph.nodes), expected_nodes_size)
        self.assertEqual(len(graph.edges), expected_edges_size)
        self.assertEqual(len(graph.hyper_edges), expected_hyper_edges_size)

    def test_invalid_graph(self):
        expected_nodes_size = 5
        expected_edges_size = 5
        expected_hyper_edges_size = 1

        graph = self._build_invalid_graph()
        graph.draw_graph()
        p10(graph)
        graph.draw_graph()

        self.assertEqual(len(graph.nodes), expected_nodes_size)
        self.assertEqual(len(graph.edges), expected_edges_size)
        self.assertEqual(len(graph.hyper_edges), expected_hyper_edges_size)

    def test_incomplete_graph(self):
        expected_nodes_size = 3
        expected_edges_size = 3
        expected_hyper_edges_size = 1

        graph = self._build_incomplete_graph()
        graph.draw_graph()
        p10(graph)
        graph.draw_graph()

        self.assertEqual(len(graph.nodes), expected_nodes_size)
        self.assertEqual(len(graph.edges), expected_edges_size)
        self.assertEqual(len(graph.hyper_edges), expected_hyper_edges_size)
