from itertools import combinations, permutations
import networkx as nx

from model.edge import Label, Square, Edge
from model.node import Node
from utils.common import calculate_x, calculate_y


def p2(graph):
    subgraph = find_isomorphic_subgraph(graph)
    if subgraph is not None:
        apply_production(graph, subgraph)


def find_isomorphic_subgraph(graph):
    for square in graph.squares:
        for edges in list(combinations(graph.edges, 5)):
            for nodes_order in list(permutations(square.nodes)):
                for hanging_node in graph.nodes:
                    if hanging_node not in nodes_order:
                        subgraph = create_subgraph(nodes_order, edges, hanging_node)
                        if validate_attributes(nodes_order, square, hanging_node) and subgraph is not None \
                                and nx.is_isomorphic(subgraph, create_base_graph()):
                            return square, edges, hanging_node
    return None


def validate_attributes(nodes, square, hanging_node):
    for node in nodes:
        if node.h != 0:
            return False
    if square.r != 1 or hanging_node.h != 1:
        return False
    return True


def create_subgraph(nodes_order, edges, hanging_node):
    if not validate_edges(edges, nodes_order, hanging_node):
        return None
    subgraph = nx.Graph()
    subgraph.add_nodes_from(list(range(6)))
    subgraph.add_edges_from(map_edges_to_ids(edges, nodes_order))
    for i in range(len(nodes_order)):
        subgraph.add_edge(5, i)
    return subgraph


def create_base_graph():
    graph = nx.Graph()
    graph.add_nodes_from(list(range(6)))
    graph.add_edges_from([(0, 1), (0, 3), (1, 2), (2, 5), (5, 3), (0, 4), (3, 4), (1, 4), (2, 4)])
    return graph


def map_node_to_id(node, nodes):
    return nodes.index(node) if node in nodes else 4


def map_edges_to_ids(edges, nodes):
    return list(map(lambda edge: (map_node_to_id(edge.n1, nodes), map_node_to_id(edge.n2, nodes)), edges))


def validate_edges(edges, nodes, node):
    all_nodes = list(nodes)
    all_nodes.append(node)
    for edge in edges:
        if edge.n1 not in all_nodes or edge.n2 not in all_nodes:
            return False
    return True


def add_node_to_square(squares, node_id, node):
    if node_id not in squares:
        squares[node_id] = [node]
    else:
        if node not in squares[node_id]:
            new_nodes = squares[node_id]
            new_nodes.append(node)
            squares[node_id] = new_nodes


def apply_production(graph, subgraph):
    square, edges, hanging_node = subgraph
    graph.squares.remove(square)
    middle_node = Node(calculate_x(square.nodes), calculate_y(square.nodes), 0, len(graph.nodes))
    graph.add_edge(Edge(middle_node, hanging_node, Label.E))

    edges_to_be_cut = []
    new_squares = {}
    for edge in edges:
        if edge.n1 != hanging_node and edge.n2 != hanging_node:
            edges_to_be_cut.append(edge)
            add_node_to_square(new_squares, edge.n1.id, edge.n1)
            add_node_to_square(new_squares, edge.n1.id, middle_node)
            add_node_to_square(new_squares, edge.n2.id, edge.n2)
            add_node_to_square(new_squares, edge.n2.id, middle_node)
        else:
            if edge.n1 == hanging_node:
                add_node_to_square(new_squares, edge.n2.id, hanging_node)
            else:
                add_node_to_square(new_squares, edge.n1.id, hanging_node)

    for edge in edges_to_be_cut:
        graph.edges.remove(edge)

        edge_nodes = [edge.n1, edge.n2]
        new_node = Node(calculate_x(edge_nodes), calculate_y(edge_nodes), 0 if edge.b == 1 else 1, len(graph.nodes))
        graph.add_node(new_node)

        graph.add_edge(Edge(edge.n1, new_node, edge.b))
        graph.add_edge(Edge(edge.n2, new_node, edge.b))
        graph.add_edge(Edge(middle_node, new_node, Label.E))

        new_squares[edge.n1.id].append(new_node)
        new_squares[edge.n2.id].append(new_node)

    for square_nodes in new_squares.values():
        graph.add_square(Square(square_nodes, 0))
