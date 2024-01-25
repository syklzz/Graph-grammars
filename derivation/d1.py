from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node
from production.p1 import apply_production as apply_p1_production
from production.p16 import p16
from production.p2 import apply_production as apply_p2_production
from production.p3 import p3
from production.p8 import p8
from production.p9 import p9

from itertools import combinations


def make_ex2_graph():
    g = Graph()

    # ramka czworokata
    node1 = Node(0, 0, 0)
    node2 = Node(4, 0, 0)
    node3 = Node(4, 4, 0)
    node4 = Node(0, 4, 0)
    g.add_nodes([node1, node2, node3, node4])

    g.add_edge(Edge(node1, node2, 0))
    g.add_edge(Edge(node3, node4, 0))
    g.add_edge(Edge(node4, node1, 0))

    # pieciokat w srodku
    node5 = Node(0.5, 0.5, 0)
    node6 = Node(2.3, 0.3, 0)
    node7 = Node(3.1, 2, 0)
    node8 = Node(2.3, 3.7, 0)
    node9 = Node(0.5, 3.5, 0)
    g.add_nodes([node5, node6, node7, node8, node9])

    g.add_edge(Edge(node5, node6, 0))
    g.add_edge(Edge(node6, node7, 0))
    g.add_edge(Edge(node7, node8, 0))
    g.add_edge(Edge(node8, node9, 0))
    g.add_edge(Edge(node9, node5, 0))

    # ekstra node w czworokacie
    node10 = Node(4, 2, 0)
    g.add_node(node10)
    g.add_edge(Edge(node7, node10, 0))

    # laczenie dwoch figur
    g.add_edge(Edge(node1, node5, 0))
    g.add_edge(Edge(node4, node9, 0))
    g.add_edge(Edge(node8, node3, 0))
    # g.add_edge(Edge(node8, node3, 0))
    g.add_edge(Edge(node6, node2, 0))
    g.add_edge(Edge(node2, node10, 0))
    g.add_edge(Edge(node3, node10, 0))

    # dodawanie hiperkrawedzi - na razie wszystkie nieoznaczone do łamania
    g.add_hyper_edge(HyperEdge([node1, node5, node9, node4], 0, Label.Q))
    g.add_hyper_edge(HyperEdge([node4, node9, node3, node8], 0, Label.Q))
    g.add_hyper_edge(HyperEdge([node1, node2, node6, node5], 0, Label.Q))
    g.add_hyper_edge(HyperEdge([node2, node10, node7, node6], 0, Label.Q))
    g.add_hyper_edge(HyperEdge([node10, node7, node8, node3], 0, Label.Q))

    g.add_hyper_edge(HyperEdge([node5, node6, node7, node8, node9], 0, Label.P))

    return g


def find_hyper_edges_with_label_and_ids(graph: Graph, label: Label, ids: list[int]):
    for hyper_edge in graph.hyper_edges:
        if hyper_edge.label == label:
            nodes = list(filter(lambda x: x.id in ids, hyper_edge.nodes))
            if len(nodes) == len(ids):
                return hyper_edge


p1_nodes = [[10, 13, 6, 12], [23, 26, 6, 27]]
def p1(graph: Graph):
    node_ids = p1_nodes.pop(0)
    hyper_edge = find_hyper_edges_with_label_and_ids(graph, Label.Q, node_ids)

    nodes = []
    for id in node_ids:
        nodes.append(next(n for n in graph.nodes if n.id == id))

    edges = []
    for n, m in combinations(nodes, 2):
        try:
            edge = next(e for e in graph.edges if ((e.n1 == n and e.n2 == m) or (e.n2 == n and e.n1 == m)))
            edges.append(edge)
        except StopIteration:
            continue

    apply_p1_production(graph, (hyper_edge, edges))

p2_nodes = [(13, [7, 2, 9, 6]), (26, [13, 16, 19, 6])]
def p2(graph: Graph):
    (hanging_id, node_ids) = p2_nodes.pop(0)

    hyper_edge = find_hyper_edges_with_label_and_ids(graph, Label.Q, node_ids)
    hanging_node = next(n for n in graph.nodes if n.id == hanging_id)

    nodes = []
    for id in node_ids:
        nodes.append(next(n for n in graph.nodes if n.id == id))

    nodes.append(hanging_node)

    edges = []
    for n, m in combinations(nodes, 2):
        try:
            edge = next(e for e in graph.edges if ((e.n1 == n and e.n2 == m) or (e.n2 == n and e.n1 == m)))
            edges.append(edge)
        except StopIteration:
            continue

    apply_p2_production(graph, (hyper_edge, edges, hanging_node))


p7_nodes = [[10, 13, 6, 12], [23, 26, 6, 27]]
def p7(graph):
    nodes = p7_nodes.pop(0)
    hyper_edge = find_hyper_edges_with_label_and_ids(graph, Label.Q, nodes)
    hyper_edge.r = 1


if __name__ == "__main__":
    graph: Graph = make_ex2_graph()

    productions = [p16, p9, p7, p8, p8, p2, p3, p1, p7, p8, p8, p2, p3, p1]

    graph.draw_graph()

    for p in productions:
        p(graph)
        graph.draw_graph()
