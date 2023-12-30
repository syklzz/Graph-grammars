from model.node import Node
from utils.common import calculate_x, calculate_y
from typing import List


class Label:
    E = 1
    Q = 2
    P = 3


class Edge:
    def __init__(self, n1: Node, n2: Node, b: int):
        self.n1 = n1
        self.n2 = n2
        self.b = b
        self.label = Label.E

    def __eq__(self, other) -> bool:
        if not isinstance(other, Edge):
            return False

        return (
            (
                (self.n1 == other.n1 and self.n2 == other.n2)
                or (self.n1 == other.n2 and self.n2 == other.n1)
            )
            and self.b == other.b
            and self.label == other.label
        )

    def __lt__(self, other) -> bool:
        return (self.n1, self.n2, self.b, self.label) < (
            other.n1,
            other.n2,
            other.b,
            other.label,
        )


class HyperEdge:
    def __init__(self, nodes: List[Node], r: int, label: Label):
        self.nodes = nodes
        self.r = r
        self.label = label
        self.central_node = Node(calculate_x(nodes), calculate_y(nodes), None)

    def __eq__(self, other) -> bool:
        if not isinstance(other, HyperEdge):
            return False

        return (
            sorted(self.nodes) == sorted(other.nodes)
            and self.r == other.r
            and self.central_node == other.central_node
            and self.label == other.label
        )

    def __repr__(self) -> str:
        return str(self.__dict__)

    def __lt__(self, other) -> bool:
        return (self.nodes, self.r, self.label, self.central_node) < (
            other.nodes,
            other.r,
            other.label,
            other.central_node,
        )
