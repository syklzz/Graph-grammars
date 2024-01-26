# from graphs import derive_base
from itertools import combinations

from model.graph import Graph

from graphs.derive_base import derive_base

from production.p1 import p1
from production.p10 import p10
from production.p2 import p2
from production.p2 import apply_production as apply_p2_production
from production.p3 import p3
from production.p7 import p7
from production.p8 import p8
from production.p17 import p17
from model.node import Node
from model.edge import Edge, HyperEdge, Label


def find_hyper_edges_with_label_and_ids(graph: Graph, label: Label, ids: list[int]):
    for hyper_edge in graph.hyper_edges:
        if hyper_edge.label == label:
            nodes = list(filter(lambda x: x.id in ids, hyper_edge.nodes))
            if len(nodes) == len(ids):
                return hyper_edge

def p2(graph: Graph, p2_nodes):
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


def derive():
    g = derive_base()

    g.draw_graph("d3-0-init.png")
    p7(g)
    g.draw_graph("d3-1-p7.png")
    p1(g)
    g.draw_graph("d3-2-p1.png")
    p7(g, [8, 10, 14, 13])
    g.draw_graph("d3-3-p7.png")
    p8(g)
    g.draw_graph("d3-4-p8.png")
    p17(g)
    g.draw_graph("d3-5-p17.png")
    p10(g)
    g.draw_graph("d3-6-p10.png")
    p3(g)
    g.draw_graph("d3-7-p3.png")
    p1(g)
    g.draw_graph("d3-8-p1.png")
    p7(g, [8, 26, 24, 23])
    g.draw_graph("d3-9-p7.png")
    p8(g, [8, 14, 19, 20])
    g.draw_graph("d3-10-p8.png")
    p8(g, [8, 13, 15, 19])
    g.draw_graph("d3-11-p8.png")
    p2(g, p2_nodes=[(24, [19, 15, 13, 8])])
    g.draw_graph("d3-12-p2.png")
    p3(g)
    g.draw_graph("d3-13-p2.png")
    p1(g)
    g.draw_graph("d3-14-p2.png")


if __name__ == "__main__":
    derive()
