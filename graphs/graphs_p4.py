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
    node6 = Node(0,1, 1)


    graph.add_nodes([node1, node2, node3, node4, node5, node6])

    graph.add_edge(Edge(node1, node2, "B1"))
    graph.add_edge(Edge(node2,node5, "B2"))
    graph.add_edge(Edge(node5, node3, "B2"))
    graph.add_edge(Edge(node3, node4, "B3"))
    graph.add_edge(Edge(node4, node6, "B4"))
    graph.add_edge(Edge(node6, node1, "B4"))

    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.Q))
    return graph

if __name__ == '__main__':
    graph = left_side_of_p4()
    graph.draw_graph()
    p4(graph)
    graph.draw_graph()

