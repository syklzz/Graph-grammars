from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node


def complex_graph_with_match():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 2, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(2, 0, 0)
    node5 = Node(1, -1, 1)
    node6 = Node(3, 0, 1)
    graph.add_nodes([node1, node2, node3, node4, node5, node6])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))
    graph.add_edge(Edge(node3, node4, 0))
    graph.add_edge(Edge(node4, node1, 0))
    graph.add_edge(Edge(node1, node5, 0))
    graph.add_edge(Edge(node5, node4, 1))
    graph.add_edge(Edge(node6, node3, 1))
    graph.add_edge(Edge(node6, node4, 1))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.Q))

    return graph


def graph_with_no_match():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 2, 1)
    node3 = Node(2, 2, 0)
    node4 = Node(2, 0, 0)
    graph.add_nodes([node1, node2, node3, node4])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))
    graph.add_edge(Edge(node3, node4, 0))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.Q))

    return graph


def graph_with_incorrect_hyper_edge_node_attribute():
    graph = Graph()

    node1 = Node(0, 0, 1)
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


def graph_with_incorrect_hyper_edge_attribute():
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

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 0, Label.Q))

    return graph


def graph_with_incorrect_hyper_edge_label():
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

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.E))

    return graph
