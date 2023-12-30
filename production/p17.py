import networkx as nx

from model.graph import Graph
from model.edge import HyperEdge, Label
from model.node import Node


def p17(graph) -> None:
    subgraph = find_isomorphic_subgraph(graph)
    if subgraph is not None:
        apply_production(graph, subgraph)


def find_isomorphic_subgraph(graph):
    hyper_edges_p = [e for e in graph.hyper_edges if e.label == Label.P]
    hyper_edges_q = [e for e in graph.hyper_edges if e.label == Label.Q]

    for hyper_edge_p in hyper_edges_p:
        for hyper_edge_q in hyper_edges_q:
            subgraph = validate_hyper_edges(graph, hyper_edge_p, hyper_edge_q)
            if subgraph:
                return subgraph
    return None


def validate_hyper_edges(graph: Graph, edge_p: HyperEdge, edge_q: HyperEdge) -> bool:
    if not (edge_p.r == 0 and edge_q.r == 1):
        return None

    common_vertex = validate_have_common_vertex(edge_p, edge_q)
    if common_vertex is None:
        return None

    result = validate_hanging_vertex(graph, common_vertex, edge_p, edge_q)
    if result is None:
        return None

    subgraph = create_subgraph(edge_p, edge_q, result)

    if nx.is_isomorphic(subgraph.to_nx(), create_base_nx_graph()):
        return subgraph
    return None


def validate_have_common_vertex(edge_p: HyperEdge, edge_q: HyperEdge):
    common_vertex = None

    for n1 in edge_p.nodes:
        for n2 in edge_q.nodes:
            if n1 == n2:
                if common_vertex:
                    return None
                common_vertex = n1
    return common_vertex


def validate_hanging_vertex(
    graph: Graph, common_vertex: Node, edge_p: HyperEdge, edge_q: HyperEdge
):
    other_p_nodes = [n for n in edge_p.nodes if n.id != common_vertex.id]
    potential_h_vertices = [
        n for n in edge_q.nodes if n.id != common_vertex.id and n.h == 1
    ]

    for potential_h_vertex in potential_h_vertices:
        for potential_accompaning_vertex in other_p_nodes:
            e1 = find_edge(graph, common_vertex, potential_h_vertex)
            e2 = find_edge(graph, potential_h_vertex, potential_accompaning_vertex)
            if e1 and e2 and e1.b == e2.b:
                return (potential_h_vertex, e1, potential_accompaning_vertex, e2)

    return None


def find_edge(graph: Graph, n1, n2):
    for e in graph.edges:
        if e.n1 == n1 and e.n2 == n2 or e.n1 == n2 and e.n2 == n1:
            return e
    return None


def validate_attributes(hyper_edge):
    for node in hyper_edge.nodes:
        if node.h != 0:
            return False
    if hyper_edge.r != 1:
        return False
    return True


def create_subgraph(edge_p: HyperEdge, edge_q: HyperEdge, result):
    (potential_h_vertex, e1, potential_accompaning_vertex, e2) = result

    subgraph = Graph()
    subgraph.add_nodes(list(set(edge_p.nodes + edge_q.nodes)))
    subgraph.add_hyper_edge(edge_p)
    subgraph.add_hyper_edge(edge_q)
    subgraph.add_edge(e1)
    subgraph.add_edge(e2)

    return subgraph


def create_base_nx_graph():
    g = nx.Graph()

    p = 8
    q = 9

    g.add_nodes_from(list(range(8)) + [p, q])
    g.add_edges_from(
        [
            (0, p),
            (1, p),
            (2, p),
            (3, p),
            (7, p),
            (1, 4),
            (2, 4),
            (2, q),
            (4, q),
            (5, q),
            (6, q),
        ]
    )
    return g


def validate_edges(edges, nodes):
    for edge in edges:
        if edge.n1 not in nodes or edge.n2 not in nodes:
            return False
    return True


def find_hyper_edge(graph: Graph, label: Label):
    return [e for e in graph.hyper_edges if e.label == label][0]


def apply_production(graph: Graph, subgraph: Graph):
    hyper_edge: HyperEdge = find_hyper_edge(subgraph, Label.P)

    graph.hyper_edges.remove(hyper_edge)

    updated_hyper_edge = HyperEdge(nodes=hyper_edge.nodes, r=1, label=Label.P)
    graph.add_hyper_edge(updated_hyper_edge)
