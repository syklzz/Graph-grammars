import unittest

from model.edge import Edge, Square
from model.graph import Graph
from model.node import Node
from production.p2 import p2


def prepare_left_side_of_production():
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


def prepare_complex_graph_with_match():
    graph = Graph()

    node1 = Node(0, 0, 0, 0)
    node2 = Node(0, 2, 0, 1)
    node3 = Node(2, 2, 0, 2)
    node4 = Node(2, 0, 0, 3)
    node5 = Node(2, 1, 1, 4)
    node6 = Node(3, 0, 0, 5)
    node7 = Node(3, 2, 1, 6)
    node8 = Node(0, 4, 1, 7)
    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))
    graph.add_edge(Edge(node3, node5, 0))
    graph.add_edge(Edge(node5, node4, 0))
    graph.add_edge(Edge(node4, node1, 0))
    graph.add_edge(Edge(node8, node2, 0))
    graph.add_edge(Edge(node8, node3, 0))
    graph.add_edge(Edge(node3, node7, 0))
    graph.add_edge(Edge(node6, node7, 0))
    graph.add_edge(Edge(node4, node6, 0))

    graph.add_square(Square([node1, node2, node3, node4], 1))
    graph.add_square(Square([node3, node7, node6, node4], 1))

    return graph

def prepare_graph_with_no_match():
    graph = Graph()

    node1 = Node(0, 0, 0, 0)
    node2 = Node(0, 2, 0, 1)
    node3 = Node(2, 2, 0, 2)
    graph.add_nodes([node1, node2, node3])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))

    graph.add_square(Square([node1, node2, node3], 1))

    return graph


class TestP2(unittest.TestCase):

    def test_production(self):
        graph = prepare_left_side_of_production()
        graph.draw_graph()
        p2(graph)
        graph.draw_graph()

    def test_on_complex_graph_with_match(self):
        graph = prepare_complex_graph_with_match()
        graph.draw_graph()
        p2(graph)
        graph.draw_graph()

    def test_on_graph_with_no_match(self):
        graph = prepare_graph_with_no_match()
        graph.draw_graph()
        p2(graph)
        graph.draw_graph()

    def test_on_empty_graph(self):
        graph = Graph()
        graph.draw_graph()
        p2(graph)
        graph.draw_graph()
