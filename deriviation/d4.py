from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node

from production.p1 import apply_production as apply_production_1
from production.p1 import validate_attributes as validate_attributes_1

from production.p2 import apply_production as apply_production_2
from production.p2 import validate_attributes as validate_attributes_2
from production.p2 import find_isomorphic_subgraph_for_d4

from production.p8 import find_midnode


def graph():
    graph = Graph()

    node1 = Node(0, 0, 0)
    node2 = Node(0, 6, 0)
    node3 = Node(6, 6, 0)
    node4 = Node(6, 3, 0)
    node5 = Node(6, 0, 0)

    node6 = Node(2, 2, 0)
    node7 = Node(2, 4, 0)
    node8 = Node(4, 4, 0)
    node9 = Node(5, 3, 0)
    node10 = Node(4, 2, 0)

    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8, node9, node10])

    graph.add_edge(Edge(node1, node2, 1))
    graph.add_edge(Edge(node2, node3, 1))
    graph.add_edge(Edge(node3, node4, 1))
    graph.add_edge(Edge(node4, node5, 1))
    graph.add_edge(Edge(node5, node1, 1))

    graph.add_edge(Edge(node1, node6, 0))
    graph.add_edge(Edge(node2, node7, 0))
    graph.add_edge(Edge(node3, node8, 0))
    graph.add_edge(Edge(node4, node9, 0))
    graph.add_edge(Edge(node5, node10, 0))

    graph.add_edge(Edge(node6, node7, 0))
    graph.add_edge(Edge(node7, node8, 0))
    graph.add_edge(Edge(node8, node9, 0))
    graph.add_edge(Edge(node9, node10, 0))
    graph.add_edge(Edge(node10, node6, 0))

    graph.add_hyper_edge(HyperEdge([node1, node2, node7, node6], 0, Label.Q))
    graph.add_hyper_edge(HyperEdge([node2, node3, node8, node7], 0, Label.Q))
    graph.add_hyper_edge(HyperEdge([node3, node4, node9, node8], 0, Label.Q))
    graph.add_hyper_edge(HyperEdge([node4, node5, node10, node9], 0, Label.Q))
    graph.add_hyper_edge(HyperEdge([node5, node1, node6, node10], 0, Label.Q))
    graph.add_hyper_edge(HyperEdge([node6, node7, node8, node9, node10], 0, Label.P))

    return graph, node3


def find_upper_left_square(g, n):
    for hyper_edge in g.hyper_edges:
        if hyper_edge.label == Label.Q and n in hyper_edge.nodes:
            for node in hyper_edge.nodes:
                if node is not n and node.y == n.y:
                    return hyper_edge
    return None


def find_lower_right_square(g, n):
    for hyper_edge in g.hyper_edges:
        if hyper_edge.label == Label.Q and n in hyper_edge.nodes:
            for node in hyper_edge.nodes:
                if node is not n and node.x == n.x:
                    return hyper_edge
    return None


def find_square_edges(g, square):
    edges = []
    for edge in g.edges:
        if edge.n1 in square.nodes and edge.n2 in square.nodes:
            edges.append(edge)
    return edges


def apply_p1(g, n):
    lower_right_square = find_lower_right_square(g, n)
    edges = find_square_edges(g, lower_right_square)

    if not validate_attributes_1(lower_right_square):
        print("Error validating p1")
    apply_production_1(g, [lower_right_square, edges])


def apply_p2(g, n):
    lower_right_square = find_upper_left_square(g, n)
    _, edges, hanging_node = find_isomorphic_subgraph_for_d4(g, lower_right_square)

    print(hanging_node)
    apply_production_2(g, [lower_right_square, edges, hanging_node])


def p7(square):
    if square.label == Label.Q and len(square.nodes) == 4 and square.r == 0:
        square.r = 1


def apply_p7(g, n):
    square = find_lower_right_square(g, n)

    p7(square)


def p8(hyper_edge1, hyper_edge2):
    common_nodes = list(set(hyper_edge1.nodes) & set(hyper_edge2.nodes))
    if common_nodes and hyper_edge1.label == hyper_edge2.label == Label.Q:
        common_node = common_nodes[0]
        if hyper_edge1.r == 0 and hyper_edge2.r == 1:
            mid_node = find_midnode(hyper_edge1, hyper_edge2, common_node)
            if mid_node.h == 1:
                hyper_edge1.r = 1
                return
        elif hyper_edge1.r == 1 and hyper_edge2.r == 0:
            mid_node = find_midnode(hyper_edge2, hyper_edge1, common_node)
            if mid_node.h == 1:
                hyper_edge2.r = 1
                return


def apply_p8(g, n):
    lower_right_square = find_lower_right_square(g, n)
    upper_left_square = find_upper_left_square(g, n)

    p8(lower_right_square, upper_left_square)


def d4():
    g, n = graph()
    g.draw_graph()

    apply_p7(g, n)
    g.draw_graph()

    apply_p1(g, n)
    g.draw_graph()

    apply_p7(g, n)
    g.draw_graph()

    apply_p8(g, n)
    g.draw_graph()

    apply_p2(g, n)
    g.draw_graph()

    apply_p1(g, n)
    g.draw_graph()

    apply_p7(g, n)
    g.draw_graph()

    apply_p8(g, n)
    g.draw_graph()

    apply_p2(g, n)
    g.draw_graph()

    apply_p1(g, n)
    g.draw_graph()


if __name__ == '__main__':
    d4()
