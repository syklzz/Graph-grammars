from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node
from production.p4 import p4


def left_side_of_p4():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)
    node5 = Node(2, 1, 1)
    node6 = Node(0, 1, 1)

    graph.add_nodes([node1, node2, node3, node4, node5, node6])

    graph.add_edge(Edge(node1, node2, "B1"))
    graph.add_edge(Edge(node2, node5, "B2"))
    graph.add_edge(Edge(node5, node3, "B2"))
    graph.add_edge(Edge(node3, node4, "B3"))
    graph.add_edge(Edge(node4, node6, "B4"))
    graph.add_edge(Edge(node6, node1, "B4"))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.Q))
    return graph


def complex_graph_with_match_p4():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)
    node5 = Node(2, 1, 1)
    node6 = Node(0, 1, 1)
    node7 = Node(0, 3, 1)
    node8 = Node(1, 3, 1)

    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8])


    graph.add_edge(Edge(node1, node2, "B1"))
    graph.add_edge(Edge(node2, node5, "B2"))
    graph.add_edge(Edge(node5, node3, "B2"))
    graph.add_edge(Edge(node3, node4, "B3"))
    graph.add_edge(Edge(node4, node6, "B4"))
    graph.add_edge(Edge(node6, node1, "B4"))
    graph.add_edge(Edge(node7, node6, "B5"))
    graph.add_edge(Edge(node7, node8, "B6"))
    graph.add_edge(Edge(node7, node3, "B7"))


    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.Q))
    return graph

def complex_graph_with_no_match_p4():
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

def graph_with_incorrect_hanging_node_attributes():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)
    node5 = Node(2, 1, 0)
    node6 = Node(0, 1, 0)

    graph.add_nodes([node1, node2, node3, node4, node5, node6])

    graph.add_edge(Edge(node1, node2, "B1"))
    graph.add_edge(Edge(node2, node5, "B2"))
    graph.add_edge(Edge(node5, node3, "B2"))
    graph.add_edge(Edge(node3, node4, "B3"))
    graph.add_edge(Edge(node4, node6, "B4"))
    graph.add_edge(Edge(node6, node1, "B4"))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.Q))
    return graph


def graph_with_incorrect_hyper_edge_attribute():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)
    node5 = Node(2, 1, 1)
    node6 = Node(0, 1, 1)

    graph.add_nodes([node1, node2, node3, node4, node5, node6])

    graph.add_edge(Edge(node1, node2, "B1"))
    graph.add_edge(Edge(node2, node5, "B2"))
    graph.add_edge(Edge(node5, node3, "B2"))
    graph.add_edge(Edge(node3, node4, "B3"))
    graph.add_edge(Edge(node4, node6, "B4"))
    graph.add_edge(Edge(node6, node1, "B4"))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 0, Label.Q))
    return graph

def graph_with_incorrect_hyper_label_attribute():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)
    node5 = Node(2, 1, 1)
    node6 = Node(0, 1, 1)

    graph.add_nodes([node1, node2, node3, node4, node5, node6])

    graph.add_edge(Edge(node1, node2, "B1"))
    graph.add_edge(Edge(node2, node5, "B2"))
    graph.add_edge(Edge(node5, node3, "B2"))
    graph.add_edge(Edge(node3, node4, "B3"))
    graph.add_edge(Edge(node4, node6, "B4"))
    graph.add_edge(Edge(node6, node1, "B4"))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.E))
    return graph



if __name__ == '__main__':
    graph = graph_with_incorrect_hyper_label_attribute()
    graph.draw_graph()
    p4(graph)
    graph.draw_graph()
