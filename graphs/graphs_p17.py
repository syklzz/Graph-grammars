from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node

from production.p17 import find_hyper_edge


def exact_match():
    g = Graph()
    n1 = Node(0, 0, 0)
    n2 = Node(2, 0, 0)
    n3 = Node(2, 2, 0)
    n4 = Node(0, 2, 0)

    n5 = Node(2, 1, 1)
    n6 = Node(4, 1, 0)
    n7 = Node(4, 2, 0)

    n8 = Node(1, 0, 0)

    g.add_nodes([n1, n2, n3, n4, n5, n6, n7, n8])

    g.add_hyper_edge(HyperEdge([n1, n2, n3, n4, n8], 0, Label.P))
    g.add_hyper_edge(HyperEdge([n3, n5, n6, n7], 1, Label.Q))

    g.add_edge(Edge(n3, n5, 2))
    g.add_edge(Edge(n5, n2, 2))

    return g


def exact_match_production():
    graph = exact_match()
    substitute_hyper_edge(graph)
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
    node8 = Node(1, 0, 0)

    node9 = Node(3.5, 0, 0)

    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8, node9])

    graph.add_edge(Edge(node1, node2, 1))
    graph.add_edge(Edge(node1, node8, 0))
    graph.add_edge(Edge(node8, node4, 0))
    graph.add_edge(Edge(node2, node5, 1))
    graph.add_edge(Edge(node2, node9, 0))
    graph.add_edge(Edge(node4, node5, 1))
    graph.add_edge(Edge(node3, node5, 1))
    graph.add_edge(Edge(node3, node7, 1))
    graph.add_edge(Edge(node5, node6, 0))
    graph.add_edge(Edge(node6, node7, 1))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4, node8], 0, Label.P))
    graph.add_hyper_edge(HyperEdge([node3, node7, node5, node6], 1, Label.Q))

    return graph


def complex_graph_with_match_production():
    graph = complex_graph_with_match()
    substitute_hyper_edge(graph)
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
    g = Graph()
    n1 = Node(0, 0, 0)
    n2 = Node(2, 0, 0)
    n3 = Node(2, 2, 0)
    n4 = Node(0, 2, 0)

    n5 = Node(2, 1, 0)
    n6 = Node(4, 1, 0)
    n7 = Node(4, 2, 0)

    n8 = Node(1, 0, 0)

    g.add_nodes([n1, n2, n3, n4, n5, n6, n7, n8])

    g.add_hyper_edge(HyperEdge([n1, n2, n3, n4, n8], 0, Label.P))
    g.add_hyper_edge(HyperEdge([n3, n5, n6, n7], 1, Label.Q))

    g.add_edge(Edge(n3, n5, 2))
    g.add_edge(Edge(n5, n2, 2))

    return g


def graph_with_incorrect_hyper_edge_attribute():
    g = Graph()
    n1 = Node(0, 0, 0)
    n2 = Node(2, 0, 0)
    n3 = Node(2, 2, 0)
    n4 = Node(0, 2, 0)

    n5 = Node(2, 1, 1)
    n6 = Node(4, 1, 0)
    n7 = Node(4, 2, 0)

    n8 = Node(1, 0, 0)

    g.add_nodes([n1, n2, n3, n4, n5, n6, n7, n8])

    g.add_hyper_edge(HyperEdge([n1, n2, n3, n4, n8], 0, Label.P))
    g.add_hyper_edge(HyperEdge([n3, n5, n6, n7], 0, Label.Q))

    g.add_edge(Edge(n3, n5, 2))
    g.add_edge(Edge(n5, n2, 2))

    return g


def graph_with_incorrect_accompanying_edge_value():
    g = Graph()
    n1 = Node(0, 0, 0)
    n2 = Node(2, 0, 0)
    n3 = Node(2, 2, 0)
    n4 = Node(0, 2, 0)

    n5 = Node(2, 1, 1)
    n6 = Node(4, 1, 0)
    n7 = Node(4, 2, 0)

    n8 = Node(1, 0, 0)

    g.add_nodes([n1, n2, n3, n4, n5, n6, n7, n8])

    g.add_hyper_edge(HyperEdge([n1, n2, n3, n4, n8], 0, Label.P))
    g.add_hyper_edge(HyperEdge([n3, n5, n6, n7], 1, Label.Q))

    g.add_edge(Edge(n3, n5, 1))
    g.add_edge(Edge(n5, n2, 2))

    return g


def substitute_hyper_edge(graph: Graph):
    hyper_edge = find_hyper_edge(graph, Label.P)

    graph.hyper_edges.remove(hyper_edge)

    new_hyper_edge = HyperEdge(nodes=hyper_edge.nodes, r=1, label=Label.P)
    graph.add_hyper_edge(new_hyper_edge)
