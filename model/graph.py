import networkx as nx

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
        positions = {}
        edge_labels = {}
        red_edges = set()

        for node in self.nodes:
            graph_nx.add_node(node)
            node_labels[node] = f"id={node.id}\nh={node.h}"
            positions[node] = (node.x, node.y)
            node_colors.append('lightblue')

        for edge in self.edges:
            graph_nx.add_edge(edge.n1, edge.n2)
            edge_labels[(edge.n1, edge.n2)] = f"B={edge.b}"

        for square in self.squares:
            graph_nx.add_node(square.central_node)
            node_labels[square.central_node] = f"Q\nr={square.r}"
            positions[square.central_node] = (square.central_node.x, square.central_node.y)
            node_colors.append('red')

            for node in square.nodes:
                graph_nx.add_edge(node, square.central_node)
                red_edges.add((node, square.central_node))
                red_edges.add((square.central_node, node))

        edge_colors = ['red' if (u, v) in red_edges or (v, u) in red_edges else 'blue' for u, v in graph_nx.edges()]

        # Draw the graph
        nx.draw_networkx_nodes(graph_nx, positions, node_color=node_colors, node_size=500)
        nx.draw_networkx_edges(graph_nx, positions, edge_color=edge_colors)

        nx.draw_networkx_labels(graph_nx,
                                positions,
                                labels=node_labels,
                                font_size=10,
                                font_color='black',
                                verticalalignment='center')

        nx.draw_networkx_edge_labels(graph_nx, positions, edge_labels=edge_labels, font_color='darkblue')

        plt.show()




