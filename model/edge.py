from model.node import Node


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
        x = 0
        y = 0
        for node in nodes:
            x += node.x
            y += node.y
        x /= len(nodes)
        y /= len(nodes)
        self.central_node = Node(x, y, None, None)