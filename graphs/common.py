from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node

def empty_graph():
    return Graph()


def left_side_of_p1():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 2, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(2, 0, 0)
    graph.add_nodes([node1, node2, node3, node4])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))
    graph.add_edge(Edge(node3, node4, 0))
    graph.add_edge(Edge(node4, node1, 1))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.Q))

    return graph


def left_side_of_p2():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 2, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(2, 0, 0)
    node5 = Node(2, 1, 1)
    graph.add_nodes([node1, node2, node3, node4, node5])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))
    graph.add_edge(Edge(node3, node5, 1))
    graph.add_edge(Edge(node5, node4, 0))
    graph.add_edge(Edge(node4, node1, 0))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.Q))

    return graph