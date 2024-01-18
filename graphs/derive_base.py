from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node


def derive_base():
    graph = Graph()

    node0 = Node(0, 0, 0)
    node1 = Node(6, 0, 0)
    node2 = Node(6, 3, 0)
    node3 = Node(6, 6, 0)
    node4 = Node(0, 6, 0)
    outer_nodes = [node0, node1, node2, node3, node4]
    node5 = Node(1.5, 1.5, 0)
    node6 = Node(4, 1.5, 0)
    node7 = Node(5, 3, 0)
    node8 = Node(4, 4.5, 0)
    node9 = Node(1.5, 4.5, 0)
    inner_nodes = [node5, node6, node7, node8, node9]

    graph.add_nodes(outer_nodes + inner_nodes)
    for i in range(len(outer_nodes)):
        graph.add_edge(Edge(outer_nodes[i-1], outer_nodes[i], 0))
        graph.add_edge(Edge(inner_nodes[i-1], inner_nodes[i], 1))
        graph.add_edge(Edge(outer_nodes[i], inner_nodes[i], 1))

    return graph


if __name__ == "__main__":
    derive_base().draw_graph()
