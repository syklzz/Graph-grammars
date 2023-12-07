from model.edge import Edge, Square
from model.graph import Graph
from model.node import Node


if __name__ == '__main__':
    g = Graph()
    node1 = Node(0, 0, 0, 1)
    node2 = Node(2, 2, 0, 2)
    node3 = Node(2, 0, 0, 3)
    node4 = Node(0, 2, 0, 4)
    g.add_nodes([node1, node2, node3, node4])
    g.add_edge(Edge(node1, node3, 'B1'))
    g.add_edge(Edge(node1, node2, 'B1'))
    g.add_edge(Edge(node2, node4, 'B1'))
    g.add_edge(Edge(node2, node4, 'B1'))

    # g.add_square(Square([node1, node2, node3, node4]))
    g.draw_graph()
