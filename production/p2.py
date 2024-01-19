from itertools import combinations
import networkx as nx

from model.edge import HyperEdge, Edge, Label
from model.node import Node
from utils.common import calculate_x, calculate_y, map_nodes_to_ids, map_edges_to_ids


def p2(graph):
    subgraph = find_isomorphic_subgraph(graph)
    if subgraph is not None:
        apply_production(graph, subgraph)


def find_isomorphic_subgraph_for_d4(graph, square):
    for hyper_edge in graph.hyper_edges:
        if hyper_edge is square:
            if hyper_edge.label == Label.Q:
                for edges in list(combinations(graph.edges, 5)):
                    for hanging_node in graph.nodes:
                        if hanging_node not in hyper_edge.nodes and validate_attributes(hyper_edge, hanging_node) \
                                and validate_edges(edges, hyper_edge.nodes, hanging_node):
                            return hyper_edge, edges, hanging_node
    return None, None, None


def find_isomorphic_subgraph(graph):
    for hyper_edges in graph.hyper_edges:
        if hyper_edges.label == Label.Q:
            for edges in list(combinations(graph.edges, 5)):
                for hanging_node in graph.nodes:
                    if hanging_node not in hyper_edges.nodes and validate_attributes(hyper_edges, hanging_node) \
                            and validate_edges(edges, hyper_edges.nodes, hanging_node) \
                            and nx.is_isomorphic(create_subgraph(hyper_edges.nodes, edges), create_base_graph()):
                        return hyper_edges, edges, hanging_node
    return None


def validate_attributes(hyper_edge, hanging_node):
    for node in hyper_edge.nodes:
        if node.h != 0:
            return False
    if hyper_edge.r != 1 or hanging_node.h != 1:
        return False
    return True


def create_subgraph(hyper_edge_nodes, edges):
    subgraph = nx.Graph()
    subgraph.add_nodes_from(map_nodes_to_ids(hyper_edge_nodes))
    subgraph.add_edges_from(map_edges_to_ids(edges))
    for i in range(len(hyper_edge_nodes)):
        subgraph.add_edge(5, i)
    return subgraph


def create_base_graph():
    graph = nx.Graph()
    graph.add_nodes_from(list(range(6)))
    graph.add_edges_from([(0, 1), (0, 3), (1, 2), (2, 5), (5, 3), (0, 4), (3, 4), (1, 4), (2, 4)])
    return graph


def validate_edges(edges, nodes, node):
    all_nodes = list(nodes)
    all_nodes.append(node)
    for edge in edges:
        if edge.n1 not in all_nodes or edge.n2 not in all_nodes:
            return False
    return True


def add_node_to_hyper_edge(hyper_edges, node_id, node):
    if node_id not in hyper_edges:
        hyper_edges[node_id] = [node]
    elif node not in hyper_edges[node_id]:
        hyper_edges[node_id].append(node)


def apply_production(graph, subgraph):
    hyper_edge, edges, hanging_node = subgraph
    graph.hyper_edges.remove(hyper_edge)

    middle_node = Node(calculate_x(hyper_edge.nodes), calculate_y(hyper_edge.nodes), 0)
    graph.add_node(middle_node)
    graph.add_edge(Edge(middle_node, hanging_node, 0))

    hanging_node.h = 0

    split_edges = []
    new_hyper_edges = {}
    for edge in edges:
        if edge.n1 != hanging_node and edge.n2 != hanging_node:
            split_edges.append(edge)
            add_node_to_hyper_edge(new_hyper_edges, edge.n1.id, edge.n1)
            add_node_to_hyper_edge(new_hyper_edges, edge.n1.id, middle_node)
            add_node_to_hyper_edge(new_hyper_edges, edge.n2.id, edge.n2)
            add_node_to_hyper_edge(new_hyper_edges, edge.n2.id, middle_node)
        else:
            node = edge.n2 if edge.n1 == hanging_node else edge.n1
            add_node_to_hyper_edge(new_hyper_edges, node.id, hanging_node)

    for edge in split_edges:
        graph.edges.remove(edge)

        edge_nodes = [edge.n1, edge.n2]
        new_node = Node(calculate_x(edge_nodes), calculate_y(edge_nodes), 0 if edge.b == 1 else 1)
        graph.add_node(new_node)

        graph.add_edge(Edge(edge.n1, new_node, edge.b))
        graph.add_edge(Edge(edge.n2, new_node, edge.b))
        graph.add_edge(Edge(middle_node, new_node, 0))

        new_hyper_edges[edge.n1.id].append(new_node)
        new_hyper_edges[edge.n2.id].append(new_node)

    for hyper_edge_nodes in new_hyper_edges.values():
        graph.add_hyper_edge(HyperEdge(hyper_edge_nodes, 0, Label.Q))
