from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node
from production.p16 import p16
from production.p4 import p4


def left_side_of_p16():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)
    node5 = Node(0, 1, 0)


    graph.add_nodes([node1, node2, node3, node4, node5])

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4, node5], 0, Label.P))
    return graph


def complex_graph_with_match_p16():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)
    node5 = Node(0, 1, 0)
    node6 = Node(0, 3, 0)
    node7 = Node(1, 4, 0)
    node8 = Node(2, 3, 0)
    node9 = Node(1, 2, 0)


    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8, node9])

    graph.add_edge(Edge(node6, node4, "B"))
    graph.add_edge(Edge(node8, node3, "B"))
    graph.add_edge(Edge(node5, node1, "B"))
    graph.add_edge(Edge(node1, node2, "B"))
    graph.add_edge(Edge(node4, node3, "B"))
    graph.add_edge(Edge(node9, node4, "B"))
    graph.add_edge(Edge(node3, node2, "B"))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4, node5], 0, Label.P))
    graph.add_hyper_edge(HyperEdge([node6, node7, node8, node9], 0, Label.Q))
    return graph


def complex_graph_with_no_match_p16():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)
    node5 = Node(0, 1, 0)
    node6 = Node(0, 3, 0)
    node7 = Node(1, 4, 0)
    node8 = Node(2, 3, 0)
    node9 = Node(1, 2, 0)

    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8, node9])

    graph.add_edge(Edge(node6, node4, "B"))
    graph.add_edge(Edge(node8, node3, "B"))
    graph.add_edge(Edge(node5, node1, "B"))
    graph.add_edge(Edge(node1, node2, "B"))
    graph.add_edge(Edge(node4, node3, "B"))
    graph.add_edge(Edge(node9, node4, "B"))
    graph.add_edge(Edge(node3, node2, "B"))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 0, Label.Q))
    graph.add_hyper_edge(HyperEdge([node6, node7, node8, node9], 0, Label.Q))
    return graph
def graph_with_incorrect_hyper_edge_attribute():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)
    node5 = Node(0, 1, 0)

    graph.add_nodes([node1, node2, node3, node4, node5])

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4, node5], 1, Label.P))
    return graph


def graph_with_incorrect_hyper_label_attribute():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)
    node5 = Node(0, 1, 0)

    graph.add_nodes([node1, node2, node3, node4, node5])

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4, node5], 0, Label.Q))
    return graph



if __name__ == '__main__':
    graph = complex_graph_with_no_match_p16()
    graph.draw_graph()
    p16(graph)
    graph.draw_graph()
