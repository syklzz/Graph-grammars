from typing import List
from model.graph import Graph
from model.node import Node
from model.edge import Label, HyperEdge
from itertools import combinations
import networkx as nx


def p8(graph: Graph, ids: List[int] = None) -> None:
    """
    Virtual adaptation propagation production.
    Applies propagation for the first pair of hyperedges found.
    """

    for i, j in combinations(range(len(graph.hyper_edges)), 2):
        hyper_edge1, hyper_edge2 = graph.hyper_edges[i], graph.hyper_edges[j]

        # If ids are given, check if all node ids in the hyperedge match the given ids
        if ids is not None:
            if not all(node.id in ids for node in hyper_edge1.nodes) and not all(node.id in ids for node in hyper_edge2.nodes):
                continue

        common_nodes = list(set(hyper_edge1.nodes) & set(hyper_edge2.nodes))
        if common_nodes and hyper_edge1.label == hyper_edge2.label == Label.Q:
            common_node = common_nodes[0]  # node3 from the slide
            if hyper_edge1.r == 0 and hyper_edge2.r == 1:
                mid_node = find_midnode(hyper_edge1, hyper_edge2, common_node)
                if mid_node and mid_node.h == 1:
                    graph.hyper_edges[i].r = 1
                    return
            elif hyper_edge1.r == 1 and hyper_edge2.r == 0:
                mid_node = find_midnode(hyper_edge2, hyper_edge1, common_node)
                if mid_node and mid_node.h == 1:
                    graph.hyper_edges[j].r = 1
                    return


def find_midnode(big: HyperEdge, small: HyperEdge, common_node: Node) -> Node:
    """
    Finds required hanging node.
    Corresponds to node 5 from the slide.
    """
    for v in big.nodes:
        if v != common_node:
            mid_x = (common_node.x + v.x) / 2
            mid_y = (common_node.y + v.y) / 2
            for u in small.nodes:
                if u.x == mid_x and u.y == mid_y:
                    return u
