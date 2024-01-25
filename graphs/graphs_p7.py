from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node


def exact_left_side():
    """
    Graph that exactly matches the left side of p7 production
    Given on slide number 16.
    """
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 1)

    graph.add_nodes([node1, node2, node3, node4])

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 0, Label.Q))
    return graph


def complex_graph_with_match():
    """
    A square with a pentagon attached to it.
    
    1 - 2 - 5
    |   |    \
    | Q |  P  6
    |   |    /
    4 - 3 - 7
    """
    graph = Graph()

    node1 = Node(0, 2, 0)
    node2 = Node(2, 2, 0)
    node3 = Node(2, 0, 0)
    node4 = Node(0, 0, 0)
    node5 = Node(4, 2, 0)
    node6 = Node(5, 1, 0)
    node7 = Node(4, 0, 0)

    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7])

    graph.add_edge(Edge(node1, node2, 0))
    graph.add_edge(Edge(node3, node2, 0))
    graph.add_edge(Edge(node4, node3, 0))
    graph.add_edge(Edge(node4, node1, 1))

    graph.add_edge(Edge(node2, node5, 0))
    graph.add_edge(Edge(node5, node6, 0))
    graph.add_edge(Edge(node6, node7, 0))
    graph.add_edge(Edge(node7, node3, 0))
    
    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 0, Label.Q))
    graph.add_hyper_edge(HyperEdge([node2, node3, node5, node6, node7], 0, Label.P))
    return graph


def graph_with_no_match():
    """ A square with a pentagon attached to it but with first node removed.
    
        2  - 5
        |     \
        |  P   6
        |     /
    4 - 3 - 7

    Returns:
        _type_: _description_
    """
    graph = Graph()

    node2 = Node(2, 2, 0)
    node3 = Node(2, 0, 0)
    node4 = Node(0, 0, 0)
    node5 = Node(4, 2, 0)
    node6 = Node(5, 1, 0)
    node7 = Node(4, 0, 0)

    graph.add_nodes([node2, node3, node4, node5, node6, node7])

    graph.add_edge(Edge(node3, node2, "B"))
    graph.add_edge(Edge(node4, node3, "B"))

    graph.add_edge(Edge(node2, node5, "B"))
    graph.add_edge(Edge(node5, node6, "B"))
    graph.add_edge(Edge(node6, node7, "B"))
    graph.add_edge(Edge(node7, node3, "B"))
    
    graph.add_hyper_edge(HyperEdge([node2, node3, node5, node6, node7], 0, Label.P))
    return graph


def graph_wrong_label():
    """
    Graph with wrong label on hyper edge.
    """
    wrong_label = Label.P
    
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)

    graph.add_nodes([node1, node2, node3, node4])

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 0, wrong_label))
    return graph 


def graph_wrong_r():
    """
    Graph with wrong r on hyper edge.
    """
    wrong_r = 1
    
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(2, 0, 0)
    node3 = Node(2, 2, 0)
    node4 = Node(0, 2, 0)

    graph.add_nodes([node1, node2, node3, node4])

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], wrong_r, Label.Q))
    return graph


if __name__=="__main__":
    print("This module is not meant to be executed directly.")
    print("But if you insist, here is a demo:")
    
    for graph in [exact_left_side(), complex_graph_with_match(), graph_with_no_match(), graph_wrong_label(), graph_wrong_r()]:
        graph.draw_graph()
