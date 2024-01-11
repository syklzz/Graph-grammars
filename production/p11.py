from collections import defaultdict
from collections.abc import Collection, Iterable
from itertools import combinations
from statistics import mean
from typing import List, NamedTuple, Set

import networkx as nx

from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node


class Subgraph(NamedTuple):
    hyper_edge: HyperEdge
    nodes: Set[Node]
    edges: List[Edge]


def p11(graph: Graph) -> None:
    """
    Breaking the five-edged element if it is marked and has two hanging nodes
    """
    subgraph = _find_isomorphic_subgraph(graph)
    if subgraph is not None:
        _apply_production(graph, subgraph)


def _find_isomorphic_subgraph(graph: Graph) -> Subgraph | None:
    valid_hyper_edges: List[HyperEdge] = [
        hyper_edge
        for hyper_edge in graph.hyper_edges
        if hyper_edge.label == Label.P
        and len(hyper_edge.nodes) == 5 # pentagon
        and hyper_edge.r == 1 # marked for breaking
        and all(node.h == 0 for node in hyper_edge.nodes) # hyper edge nodes are not hanging nodes
    ]

    subgraphs = (
        Subgraph(hyper_edge, _get_nodes_from_edges(edges), edges)
            for hyper_edge in valid_hyper_edges
            for edges in combinations(graph.edges, 7)
            if _validate_subgraph(edges, hyper_edge.nodes)
    )
    
    return next(subgraphs, None)


def _get_nodes_from_edges(edges: List[Edge]) -> Set[Node]:
    return set([edge.n1 for edge in edges] + [edge.n2 for edge in edges])


def _validate_subgraph(edges: List[Edge], corner_nodes: List[Node]) -> bool:
    edge_nodes = _get_nodes_from_edges(edges)
    hanging_nodes = list(edge_nodes - set(corner_nodes))

    are_nodes_in_edges = _validate_nodes_in_edges(edge_nodes, corner_nodes)
    are_hanging_nodes_valid = _validate_hanging_nodes(hanging_nodes)

    base_graph = _create_base_graph()
    subgraph = _create_subgraph(edges, corner_nodes)
    is_isomorphic = nx.is_isomorphic(base_graph, subgraph)
    
    return are_nodes_in_edges and are_hanging_nodes_valid and is_isomorphic


def _validate_nodes_in_edges(edge_nodes: List[Node], nodes: List[Node]) -> bool:
    edge_node_ids = set(edge_node.id for edge_node in edge_nodes)
    return all(node.id in edge_node_ids for node in nodes)


def _validate_hanging_nodes(hanging_nodes: List[Node]) -> bool:
    only_two_hanging_nodes = len(hanging_nodes) == 2
    hanging_nodes_have_h_1 = all(node.h == 1 for node in hanging_nodes)

    return only_two_hanging_nodes and hanging_nodes_have_h_1

def _create_base_graph() -> nx.Graph:
    """Graph with five-edged element and a hyperEdge with label P in the middle.
    The left side of P11 production. Given on slide number 25.
    
    "corner" nodes: 1, 2, 5, 3, 4
    "hanging" nodes: 6, 7
    
    """
    corner_and_hanging_nodes_edge_list = [(1, 6), (6, 2), (2, 5), (5, 3), (3, 4), (4, 7), (7, 1)]
    hyper_edge_edge_list = [(0, 1), (0, 2), (0, 5), (0, 3), (0, 4)]
    return nx.Graph(corner_and_hanging_nodes_edge_list + hyper_edge_edge_list)


def _create_subgraph(edges: List[Edge], corner_nodes: List[Node]) -> nx.Graph:
    """Creates a subgraph from the given edges and corner nodes.

    arguments:
    edges -- list of edges (label E)
    corner_nodes -- list of nodes connected with a hyperEdge with label P
    
    returns:
    nx.Graph object with edges and corner nodes from the arguments
    """

    ARBITRARY_HYPER_EDGE_ID = -1
    
    corner_and_hanging_nodes_edge_list = [(edge.n1.id, edge.n2.id) for edge in edges]
    hyper_edge_edge_list = [(ARBITRARY_HYPER_EDGE_ID, node.id) for node in corner_nodes]
    
    return nx.Graph(corner_and_hanging_nodes_edge_list + hyper_edge_edge_list)


def _apply_production(graph: Graph, subgraph: Subgraph):
    hyper_edge = subgraph.hyper_edge
    edges = subgraph.edges

    graph.hyper_edges.remove(hyper_edge)

    middle_node = Node(
        x=mean(n.x for n in hyper_edge.nodes),
        y=mean(n.y for n in hyper_edge.nodes),
        h=0,
    )

    graph.add_node(middle_node)

    new_hyper_edges = {node.id: [node, middle_node] for node in [*hyper_edge.nodes]}

    for edge in edges:
        if edge.n1.h == 1:
            new_edge = Edge(edge.n1, middle_node, 0)
            if not any(e.n1 == new_edge.n1 and e.n2 == new_edge.n2 and e.b == new_edge.b for e in graph.edges):
                graph.add_edge(new_edge)
                new_hyper_edges[edge.n2.id].append(edge.n1)
            continue
        elif edge.n2.h == 1:
            new_hyper_edges[edge.n1.id].append(edge.n2)
            continue

        # Check if the edge already exists in the graph
        new_edge = Edge(middle_node, edge.n2, 0)
        if not any(e.n1 == new_edge.n1 and e.n2 == new_edge.n2 and e.b == new_edge.b for e in graph.edges):
            graph.edges.remove(edge)

            edge_nodes = [edge.n1, edge.n2]
            new_node = Node(
                mean(n.x for n in edge_nodes),
                mean(n.y for n in edge_nodes),
                int(edge.b != 1),
            )

            graph.add_node(new_node)
            graph.add_edge(Edge(edge.n1, new_node, edge.b))
            graph.add_edge(Edge(edge.n2, new_node, edge.b))
            graph.add_edge(Edge(middle_node, new_node, 0))

            new_hyper_edges[edge.n1.id].append(new_node)
            new_hyper_edges[edge.n2.id].append(new_node)

    for hyper_edges_nodes in new_hyper_edges.values():
        graph.add_hyper_edge(HyperEdge(hyper_edges_nodes, 0, Label.Q))
