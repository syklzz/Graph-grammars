import unittest

from model.edge import Edge, Square
from model.graph import Graph
from model.node import Node
from production.p2 import p2


def prepare_graph():
    graph = Graph()

    node1 = Node(0, 0, 0, 0)
    node2 = Node(0, 2, 0, 1)
    node3 = Node(2, 2, 0, 2)
    node4 = Node(2, 0, 0, 3)
    node5 = Node(2, 1, 1, 4)
    graph.add_nodes([node1, node2, node3, node4, node5])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))
    graph.add_edge(Edge(node3, node5, 0))
    graph.add_edge(Edge(node5, node4, 0))
    graph.add_edge(Edge(node4, node1, 0))

    graph.add_square(Square([node1, node2, node3, node4], 1))

    return graph

def expected_graph():
    return Graph()


class TestP2(unittest.TestCase):

    def test_production(self):
        graph = prepare_graph()
        # graph.draw_graph()
        p2(graph)
        # graph.draw_graph()
        self.assertTrue(graph.equals(expected_graph()))
