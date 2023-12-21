import unittest

from model.graph import Graph
from model.node import Node
from model.edge import Edge, HyperEdge, Label
from production.p9 import p9


class TestP1(unittest.TestCase):
    @staticmethod
    def _build_valid_graph() -> Graph:
        graph = Graph()

        node1 = Node(0, 0, 0)
        node2 = Node(0, 2, 0)
        node3 = Node(2, 2, 0)
        node4 = Node(2.5, 1, 0)
        node5 = Node(2, 0, 0)
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

        graph.add_hyper_edge(HyperEdge([node1, node2, node3], r=1, label=Label.Q))

        return graph

    def test_valid_graph(self):
        expected_nodes_size = 11
        expected_edges_size = 15
        expected_hyper_edges_size = 5

        graph = self._build_valid_graph()
        graph.draw_graph()
        p9(graph)
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
        p9(graph)
        graph.draw_graph()

        self.assertEqual(len(graph.nodes), expected_nodes_size)
        self.assertEqual(len(graph.edges), expected_edges_size)
        self.assertEqual(len(graph.hyper_edges), expected_hyper_edges_size)

    def test_incomplete_graph(self):
        expected_nodes_size = 3
        expected_edges_size = 3
        expected_hyper_edges_size = 1

        graph = self._build_invalid_graph()
        graph.draw_graph()
        p9(graph)
        graph.draw_graph()

        self.assertEqual(len(graph.nodes), expected_nodes_size)
        self.assertEqual(len(graph.edges), expected_edges_size)
        self.assertEqual(len(graph.hyper_edges), expected_hyper_edges_size)
