from model.node import Node
from utils.common import calculate_x, calculate_y


class Label:
    E = 1
    Q = 2
    P = 3


class Edge:
    def __init__(self, n1: Node, n2: Node, b):
        self.n1 = n1
        self.n2 = n2
        self.b = b
        self.label = Label.E


class HyperEdge:
    def __init__(self, nodes, r, label):
        self.nodes = nodes
        self.r = r
        self.label = label
        self.central_node = Node(calculate_x(nodes), calculate_y(nodes), None)
