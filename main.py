from model.edge import Edge, Square
from model.graph import Graph
from model.node import Node


if __name__ == '__main__':
    g = Graph()
    node1 = Node(1, 2, 3, 11)
    node3 = Node(6, 7, 1, 22)
    node4 = Node(9, 7, 1, 23)
    node5 = Node(14, 8, 1, 24)
    g.add_edge(Edge(node1, Node(3, 4, 5, 12)))
    g.add_edge(Square([node1, node3, node4, node5]))
    g.draw_graph()