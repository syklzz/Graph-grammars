from typing import List
from model.node import Node
from model.edge import Edge, HyperEdge, Label
import networkx as nx

import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.nodes: List[Node] = []
        self.edges: List[Edge] = []
        self.hyper_edges: List[HyperEdge] = []
        self.new_node_id: int = 0

    def add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)

    def add_nodes(self, nodes: List[Node]) -> None:
        for node in nodes:
            self.add_node(node)

    def add_node(self, node: Node) -> None:
        node.id = self.new_node_id
        self.nodes.append(node)
        self.new_node_id += 1

    def add_hyper_edge(self, hyper_edge: HyperEdge) -> None:
        self.hyper_edges.append(hyper_edge)

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

        for hyper_edge in self.hyper_edges:
            graph_nx.add_node(hyper_edge.central_node)

            if hyper_edge.label == Label.Q:
                node_labels[hyper_edge.central_node] = f"Q\nr={hyper_edge.r}"
            if hyper_edge.label == Label.P:
                node_labels[hyper_edge.central_node] = f"P\nr={hyper_edge.r}"
            positions[hyper_edge.central_node] = (
                hyper_edge.central_node.x, hyper_edge.central_node.y)
            node_colors.append('red')

            for node in hyper_edge.nodes:
                graph_nx.add_edge(node, hyper_edge.central_node)
                red_edges.add((node, hyper_edge.central_node))
                red_edges.add((hyper_edge.central_node, node))

        edge_colors = ['red' if (u, v) in red_edges or (
            v, u) in red_edges else 'blue' for u, v in graph_nx.edges()]

        # Draw the graph
        nx.draw_networkx_nodes(graph_nx, positions,
                               node_color=node_colors, node_size=500)
        nx.draw_networkx_edges(graph_nx, positions, edge_color=edge_colors)

        nx.draw_networkx_labels(graph_nx,
                                positions,
                                labels=node_labels,
                                font_size=10,
                                font_color='black',
                                verticalalignment='center')

        nx.draw_networkx_edge_labels(
            graph_nx, positions, edge_labels=edge_labels, font_color='darkblue')

        plt.show()
