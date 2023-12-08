import unittest

from model.edge import Edge, Square
from model.graph import Graph
from model.node import Node
from production.p1 import p1


def prepare_left_side_of_production():
    graph = Graph()

    node1 = Node(0, 0, 0, 0)
    node2 = Node(0, 2, 0, 1)
    node3 = Node(2, 2, 0, 2)
    node4 = Node(2, 0, 0, 3)
    graph.add_nodes([node1, node2, node3, node4])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))
    graph.add_edge(Edge(node3, node4, 0))
    graph.add_edge(Edge(node4, node1, 0))

    graph.add_square(Square([node1, node2, node3, node4], 1))

    return graph


def prepare_complex_graph_with_match():
    graph = Graph()

    node1 = Node(0, 0, 0, 0)
    node2 = Node(0, 2, 0, 1)
    node3 = Node(2, 2, 0, 2)
    node4 = Node(2, 0, 0, 3)
    node5 = Node(1, -1, 1, 4)
    node6 = Node(3, 0, 1, 5)
    graph.add_nodes([node1, node2, node3, node4, node5, node6])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))
    graph.add_edge(Edge(node3, node4, 0))
    graph.add_edge(Edge(node4, node1, 0))
    graph.add_edge(Edge(node1, node5, 0))
    graph.add_edge(Edge(node5, node4, 1))
    graph.add_edge(Edge(node6, node3, 1))
    graph.add_edge(Edge(node6, node4, 1))

    graph.add_square(Square([node1, node2, node3, node4], 1))

    return graph


def prepare_graph_with_no_match():
    graph = Graph()

    node1 = Node(0, 0, 0, 0)
    node2 = Node(0, 2, 1, 1)
    node3 = Node(2, 2, 0, 2)
    node4 = Node(2, 0, 0, 3)
    graph.add_nodes([node1, node2, node3, node4])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))
    graph.add_edge(Edge(node3, node4, 0))

    graph.add_square(Square([node1, node2, node3, node4], 1))

    return graph


class TestP1(unittest.TestCase):

    def test_on_left_side_of_production(self):
        graph = prepare_left_side_of_production()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

    def test_on_complex_graph_with_match(self):
        graph = prepare_complex_graph_with_match()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

    def test_on_graph_with_no_match(self):
        graph = prepare_graph_with_no_match()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()

    def test_on_empty_graph(self):
        graph = Graph()
        graph.draw_graph()
        p1(graph)
        graph.draw_graph()
