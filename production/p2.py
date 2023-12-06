from itertools import combinations
import networkx as nx


def p2(graph):
    pass


def find_isomorphic_subgraph(graph):
    for square in graph.squares:
        for edge in list(combinations(graph.edges)):
            for node in graph.nodes:
                subgraph = create_subgraph()

            if nx.is_isomorphic(subgraph, create_base_graph):
                return None
    return None


def create_subgraph(square, edges):
    return None


def create_base_graph():
    graph = nx.Graph()
    graph.add_nodes_from(list(range(6)))
    graph.add_edges_from([(0, 1), (0, 2), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
    return graph
