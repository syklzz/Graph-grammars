from collections import defaultdict
from collections.abc import Collection, Iterable
from functools import partial
from itertools import combinations, count
from statistics import mean
from typing import NamedTuple

import networkx as nx

from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node


class Subgraph(NamedTuple):
    hyper_edge: HyperEdge
    edges: Collection[Edge]


def p9(graph: Graph):
    if (subgraph := _find_subgraph(graph)) is not None:
        _apply_production(graph, subgraph)


def _find_subgraph(graph: Graph) -> Subgraph | None:
    valid_hyper_edges: Iterable[HyperEdge] = (
        hyper_edge
        for hyper_edge in graph.hyper_edges
        if hyper_edge.label == Label.P
        and all(node.h == 0 for node in hyper_edge.nodes)
        and hyper_edge.r == 1
    )

    return next(
        (
            Subgraph(hyper_edge, edges)
            for hyper_edge in valid_hyper_edges
            for edges in combinations(graph.edges, 5)
            if _validate_subgraph(edges, hyper_edge.nodes)
        ),
        None,
    )


def _validate_subgraph(edges: Collection[Edge], nodes: Collection[Node]) -> bool:
    return _validate_edges(edges, nodes) and nx.is_isomorphic(
        _create_subgraph(edges), _create_base_graph()
    )


def _validate_edges(edges: Collection[Edge], nodes: Collection[Node]) -> bool:
    return all(edge.n1 in nodes and edge.n2 in nodes for edge in edges)


def _create_base_graph() -> nx.Graph:
    return nx.Graph(
        [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]
    )


def _create_subgraph(edges: Collection[Edge]) -> nx.Graph:
    remap: dict[int, int] = defaultdict(partial(next, count()))
    subgraph = nx.Graph((remap[edge.n1.id], remap[edge.n2.id]) for edge in edges)
    subgraph.add_edges_from((remap[None], node) for node in [*remap.values()])
    return subgraph


def _apply_production(graph: Graph, subgraph: Subgraph):
    hyper_edge, edges = subgraph
    graph.hyper_edges.remove(hyper_edge)

    middle_node = Node(
        x=mean(n.x for n in hyper_edge.nodes),
        y=mean(n.y for n in hyper_edge.nodes),
        h=0,
    )

    graph.add_node(middle_node)

    new_hyper_edges = {node.id: [node, middle_node] for node in hyper_edge.nodes}

    for edge in edges:
        graph.edges.remove(edge)

        edge_nodes = [edge.n1, edge.n2]
        new_node = Node(
            x=mean(n.x for n in edge_nodes),
            y=mean(n.y for n in edge_nodes),
            h=int(edge.b != 1),
        )

        graph.add_node(new_node)
        graph.add_edge(Edge(edge.n1, new_node, edge.b))
        graph.add_edge(Edge(edge.n2, new_node, edge.b))
        graph.add_edge(Edge(middle_node, new_node, 0))

        new_hyper_edges[edge.n1.id].append(new_node)
        new_hyper_edges[edge.n2.id].append(new_node)

    for hyper_edges_nodes in new_hyper_edges.values():
        graph.add_hyper_edge(HyperEdge(hyper_edges_nodes, 0, Label.Q))
