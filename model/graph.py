import networkx as nx

from model.edge import Label

import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.squares = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_node(self, node):
        self.nodes.append(node)

    def add_square(self, square):
        self.squares.append(square)

    def draw_graph(self):
        graph_nx = nx.Graph()
        node_labels = {}
        node_colors = []

        for node in self.nodes:
            graph_nx.add_node(node)
            node_labels[node] = 'N'
            node_colors.append('lightblue')

        edge_colors = []
        for edge in self.edges:
            graph_nx.add_edge(edge.n1, edge.n2)
            edge_colors.append('blue' if edge.label == Label.E else 'red')
        for square in self.squares:
            node_labels[square.central_node] = 'Q'
            node_colors.append('red')
            graph_nx.add_node(square.central_node)

            for node in square.nodes:
                graph_nx.add_edge(node, square.central_node)
                edge_colors.append('red')

        pos = nx.spring_layout(graph_nx)
        nx.draw_networkx_nodes(graph_nx, pos, node_color=node_colors, node_size=500)
        nx.draw_networkx_edges(graph_nx, pos, edge_color=edge_colors)
        nx.draw_networkx_labels(graph_nx, pos, labels=node_labels, font_size=15)

        plt.show()
