from itertools import combinations
import networkx as nx

from model.edge import Edge, HyperEdge, Label
from model.node import Node
from utils.common import calculate_x, calculate_y, map_edges_to_ids, map_nodes_to_ids


def p1(graph):
    subgraph = find_isomorphic_subgraph(graph)
    if subgraph is not None:
        apply_production(graph, subgraph)


def find_isomorphic_subgraph(graph):
    for hyper_edge in graph.hyper_edges:
        if hyper_edge.label == Label.Q:
            for edges in list(combinations(graph.edges, 4)):
                edges_bool = validate_edges(edges, hyper_edge.nodes)
                atributes = validate_attributes(hyper_edge)
                created_subgraph = create_subgraph(hyper_edge.nodes, edges)
                is_isomorphic = nx.is_isomorphic(created_subgraph, create_base_graph())
                
                if edges_bool and atributes and is_isomorphic:
                    return hyper_edge, edges
    return None


def validate_attributes(hyper_edge):
    for node in hyper_edge.nodes:
        if node.h != 0:
            return False
    if hyper_edge.r != 1:
        return False
    return True


def create_subgraph(hyper_edge_nodes, edges):
    subgraph = nx.Graph()
    HYPER_NODE_ID = -1
    nodes_ids = map_nodes_to_ids(hyper_edge_nodes)
    subgraph.add_nodes_from(nodes_ids)
    subgraph.add_edges_from(map_edges_to_ids(edges))
    subgraph.add_node(HYPER_NODE_ID)
    for i in nodes_ids:
        subgraph.add_edge(HYPER_NODE_ID, i)
    return subgraph


def create_base_graph():
    graph = nx.Graph()
    graph.add_nodes_from(list(range(5)))
    graph.add_edges_from([(0, 1), (0, 2), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
    return graph


def validate_edges(edges, nodes):
    for edge in edges:
        if edge.n1 not in nodes or edge.n2 not in nodes:
            return False
    return True


def apply_production(graph, subgraph):
    hyper_edge, edges = subgraph
    graph.hyper_edges.remove(hyper_edge)

    middle_node = Node(calculate_x(hyper_edge.nodes), calculate_y(hyper_edge.nodes), 0)
    graph.add_node(middle_node)

    new_hyper_edges = {}
    for node in hyper_edge.nodes:
        new_hyper_edges[node.id] = [node, middle_node]

    for edge in edges:
        graph.edges.remove(edge)

        edge_nodes = [edge.n1, edge.n2]
        new_node = Node(calculate_x(edge_nodes), calculate_y(edge_nodes), 0 if edge.b == 1 else 1)
        graph.add_node(new_node)

        graph.add_edge(Edge(edge.n1, new_node, edge.b))
        graph.add_edge(Edge(edge.n2, new_node, edge.b))
        graph.add_edge(Edge(middle_node, new_node, 0))

        new_hyper_edges[edge.n1.id].append(new_node)
        new_hyper_edges[edge.n2.id].append(new_node)

    for hyper_edges_nodes in new_hyper_edges.values():
        graph.add_hyper_edge(HyperEdge(hyper_edges_nodes, 0, Label.Q))

