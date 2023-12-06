import networkx as nx

from model.edge import Edge, Square, Label

import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.squares = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_node(self, vertex):
        self.nodes.append(vertex)

    def add_square(self, square):
        self.squares.append(square)

    def is_isomorphic_with(self, graph_to_compare):
        self_nx = nx.Graph()
        self_nx.add_nodes_from(self.nodes)
        self_nx.add_edges_from(self.edges)

        graph_to_compare_nx = nx.Graph()
        graph_to_compare_nx.add_nodes_from(graph_to_compare.nodes)
        graph_to_compare_nx.add_edges_from(graph_to_compare.edges)

        return nx.is_isomorphic(self_nx, graph_to_compare_nx)

    def draw_graph(self):
        graph_nx = nx.Graph()
        node_labels = {}
        node_colors = []

        for v in self.nodes:
            graph_nx.add_node(v)
            node_labels[v] = 'E'
            node_colors.append('lightblue')

        edge_colors = []
        for edge in self.edges:
            if isinstance(edge, Edge):
                graph_nx.add_edge(edge.n1, edge.n2)
                edge_colors.append('red' if edge.label == Label.E else 'blue')
            elif isinstance(edge, Square):
                node_labels[edge.central_node] = 'Q'
                node_colors.append('blue')
                graph_nx.add_node(edge.central_node)

                for node in edge.nodes:
                    graph_nx.add_edge(node, edge.central_node)
                    edge_colors.append('blue')

        pos = nx.spring_layout(graph_nx)
        nx.draw_networkx_nodes(graph_nx, pos, node_color=node_colors, node_size=500)
        nx.draw_networkx_edges(graph_nx, pos, edge_color=edge_colors)
        nx.draw_networkx_labels(graph_nx, pos, labels=node_labels, font_size=15)

        plt.show()