from model.node import Node
from utils.common import calculate_x, calculate_y


class Label:
    E = 1
    Q = 2


class Edge:
    def __init__(self, n1: Node, n2: Node, b):
        self.n1 = n1
        self.n2 = n2
        self.label = Label.E
        self.b = b


class Square:
    def __init__(self, nodes, r):
        self.nodes = nodes
        self.r = r
        self.label = Label.Q
        self.central_node = Node(calculate_x(nodes), calculate_y(nodes), None, None)
