from itertools import combinations, permutations
import networkx as nx

from model.edge import Edge, Square
from model.node import Node
from utils.common import calculate_x, calculate_y


def p1(graph):
    subgraph = find_isomorphic_subgraph(graph)
    if subgraph is not None:
        apply_production(graph, subgraph)


def find_isomorphic_subgraph(graph):
    for square in graph.squares:
        for edges in list(combinations(graph.edges, 4)):
            for nodes_order in list(permutations(square.nodes)):
                subgraph = create_subgraph(nodes_order, edges)
                if validate_attributes(nodes_order, square) and subgraph is not None \
                        and nx.is_isomorphic(subgraph, create_base_graph()):
                    return square, edges
    return None


def validate_attributes(nodes, square):
    for node in nodes:
        if node.h != 0:
            return False
    if square.r != 1:
        return False
    return True


def create_subgraph(nodes_order, edges):
    if not validate_edges(edges, nodes_order):
        return None
    subgraph = nx.Graph()
    subgraph.add_nodes_from(list(range(5)))
    subgraph.add_edges_from(map_edges_to_ids(edges, nodes_order))
    subgraph.add_node(4)
    for i in range(len(nodes_order)):
        subgraph.add_edge(4, i)
    return subgraph


def create_base_graph():
    graph = nx.Graph()
    graph.add_nodes_from(list(range(5)))
    graph.add_edges_from([(0, 1), (0, 2), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
    return graph


def map_edges_to_ids(edges, nodes):
    return list(map(lambda edge: (nodes.index(edge.n1), nodes.index(edge.n2)), edges))


def validate_edges(edges, nodes):
    for edge in edges:
        if edge.n1 not in nodes or edge.n2 not in nodes:
            return False
    return True


def apply_production(graph, subgraph):
    square, edges = subgraph
    graph.squares.remove(square)

    middle_node = Node(calculate_x(square.nodes), calculate_y(square.nodes), 0, len(graph.nodes))
    graph.add_node(middle_node)

    new_squares = {}
    for node in square.nodes:
        new_squares[node.id] = [node, middle_node]

    for edge in edges:
        graph.edges.remove(edge)

        edge_nodes = [edge.n1, edge.n2]
        new_node = Node(calculate_x(edge_nodes), calculate_y(edge_nodes), 0 if edge.b == 1 else 1, len(graph.nodes))
        graph.add_node(new_node)

        graph.add_edge(Edge(edge.n1, new_node, edge.b))
        graph.add_edge(Edge(edge.n2, new_node, edge.b))
        graph.add_edge(Edge(middle_node, new_node, None))

        new_squares[edge.n1.id].append(new_node)
        new_squares[edge.n2.id].append(new_node)

    for square_nodes in new_squares.values():
        graph.add_square(Square(square_nodes, 0))

