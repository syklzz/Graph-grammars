from itertools import combinations, permutations
import networkx as nx

from model.node import Node


def p1(graph):
    subgraph = find_isomorphic_subgraph(graph)
    if subgraph is not None:
        apply_production(graph, subgraph)


def find_isomorphic_subgraph(graph):
    for square in graph.squares:
        for edges in list(combinations(graph.edges, 4)):
            for nodes in list(permutations(square.nodes)):
                subgraph = create_subgraph(nodes, edges)
                if subgraph is not None and nx.is_isomorphic(subgraph, create_base_graph()):
                    return square, nodes, edges
    return None


def create_subgraph(nodes, edges):
    if not validate_edges(nodes, edges):
        return None
    subgraph = nx.Graph()
    subgraph.add_nodes_from(map_nodes_to_ids(nodes))
    subgraph.add_edges_from(map_edges_to_ids(nodes, edges))
    return subgraph


def create_base_graph():
    graph = nx.Graph()
    graph.add_nodes_from(list(range(5)))
    graph.add_edges_from([(0, 1), (0, 2), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
    return graph


def map_nodes_to_ids(nodes):
    return list(range(len(nodes)))


def map_edges_to_ids(edges, nodes):
    return list(map(lambda edge: (nodes.index(edge.n1), nodes.index(edge.n2)), edges))


def validate_edges(edges, nodes):
    for edge in edges:
        if edge.n1 not in nodes or edge.n2 not in nodes:
            return False
    return True


def apply_production(graph, subgraph):
    square, nodes, edges = subgraph

    graph.squares.remove(square)

    middle_node = Node(calculate_x(nodes), calculate_y(nodes), 0, len(graph.nodes))

    for edge in edges:
        edge_nodes = [edge.n1, edge.n2]
        new_node = Node(calculate_x(edge_nodes), calculate_y(edge_nodes), -edge.b, len(graph.nodes))
        graph.add_nodes(new_node)
        graph.add_node_on_edge(node, edge)
        graph.add_square()



def calculate_x(nodes):
    return sum(list(map(lambda node: node.x, nodes))) / len(nodes)


def calculate_y(nodes):
    return sum(list(map(lambda node: node.y, nodes))) / len(nodes)
