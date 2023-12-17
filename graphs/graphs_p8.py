from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node


def left_side_of_p8():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 2, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(2, 0, 0)
    node5 = Node(2, 1, 1)
    node6 = Node(4, 1, 0)
    node7 = Node(4, 2, 0)
    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7])

    graph.add_edge(Edge(node2, node5, 0))
    graph.add_edge(Edge(node3, node5, 0))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 0, Label.Q))
    graph.add_hyper_edge(HyperEdge([node3, node7, node5, node6], 1, Label.Q))

    return graph


def complex_graph_with_match():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 2, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(2, 0, 0)
    node5 = Node(2, 1, 1)
    node6 = Node(4, 1, 0)
    node7 = Node(4, 2, 0)
    node8 = Node(4, 0, 0)

    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8])

    graph.add_edge(Edge(node1, node2, 1))
    graph.add_edge(Edge(node1, node4, 0))
    graph.add_edge(Edge(node2, node5, 1))
    graph.add_edge(Edge(node2, node8, 0))
    graph.add_edge(Edge(node3, node4, 1))
    graph.add_edge(Edge(node3, node5, 0))
    graph.add_edge(Edge(node3, node7, 1))
    graph.add_edge(Edge(node5, node6, 0))
    graph.add_edge(Edge(node6, node7, 1))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 0, Label.Q))
    graph.add_hyper_edge(HyperEdge([node3, node7, node5, node6], 1, Label.Q))

    return graph


def graph_with_no_match():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 2, 0)
    node3 = Node(2, 2, 0)
    graph.add_nodes([node1, node2, node3])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node2, node3, 0))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3], 1, Label.Q))

    return graph


def graph_with_incorrect_hanging_node_attribute():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 2, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(2, 0, 0)
    node5 = Node(2, 1, 37)
    node6 = Node(4, 1, 0)
    node7 = Node(4, 2, 0)
    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7])

    graph.add_edge(Edge(node2, node5, 0))
    graph.add_edge(Edge(node3, node5, 0))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 0, Label.Q))
    graph.add_hyper_edge(HyperEdge([node3, node7, node5, node6], 1, Label.Q))

    return graph


def graph_with_incorrect_hyper_edge_attribute():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 2, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(2, 0, 0)
    node5 = Node(2, 1, 1)
    node6 = Node(4, 1, 0)
    node7 = Node(4, 2, 0)
    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7])

    graph.add_edge(Edge(node2, node5, 0))
    graph.add_edge(Edge(node3, node5, 0))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 42, Label.Q))
    graph.add_hyper_edge(HyperEdge([node3, node7, node5, node6], 0, Label.Q))

    return graph


def graph_with_incorrect_hyper_edge_label():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 2, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(2, 0, 0)
    node5 = Node(2, 1, 1)
    node6 = Node(4, 1, 0)
    node7 = Node(4, 2, 0)
    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7])

    graph.add_edge(Edge(node2, node5, 0))
    graph.add_edge(Edge(node3, node5, 0))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 0, "x"))
    graph.add_hyper_edge(HyperEdge([node3, node7, node5, node6], 1, "D"))

    return graph
