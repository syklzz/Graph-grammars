from typing import List
from model.node import Node
from model.edge import Edge, HyperEdge, Label
import networkx as nx

import matplotlib.pyplot as plt

from utils.common import map_edges_to_ids, map_nodes_to_ids


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
        if node.id is None:
            node.id = self.new_node_id
        self.nodes.append(node)
        self.new_node_id = max([node.id for node in self.nodes]) + 1

    def add_hyper_edge(self, hyper_edge: HyperEdge) -> None:
        self.hyper_edges.append(hyper_edge)

    def draw_graph(self, filepath: str = None):
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
            node_colors.append("lightblue")

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
                hyper_edge.central_node.x,
                hyper_edge.central_node.y,
            )
            node_colors.append("red")

            for node in hyper_edge.nodes:
                graph_nx.add_edge(node, hyper_edge.central_node)
                red_edges.add((node, hyper_edge.central_node))
                red_edges.add((hyper_edge.central_node, node))

        edge_colors = [
            "red" if (u, v) in red_edges or (v, u) in red_edges else "blue"
            for u, v in graph_nx.edges()
        ]

        # Draw the graph
        plt.figure(figsize=(24, 18))

        nx.draw_networkx_nodes(
            graph_nx, positions, node_color=node_colors, node_size=500
        )
        nx.draw_networkx_edges(graph_nx, positions, edge_color=edge_colors)

        nx.draw_networkx_labels(
            graph_nx,
            positions,
            labels=node_labels,
            font_size=15,
            font_color="black",
            verticalalignment="center",
        )

        nx.draw_networkx_edge_labels(
            graph_nx,
            positions,
            edge_labels=edge_labels,
            font_color="darkblue",
            font_size=15,
        )

        if filepath is not None: 
            plt.savefig(filepath)
        else:
            plt.show()

    def to_nx(self) -> nx.Graph:
        graph = nx.Graph()
        graph.add_nodes_from(map_nodes_to_ids(self.nodes))
        graph.add_edges_from(map_edges_to_ids(self.edges))

        for hyperedge in self.hyper_edges:
            nodes = hyperedge.nodes

            node_id = "".join([str(n.id) for n in nodes])
            graph.add_node(node_id)

            edges = [(node_id, node.id) for node in nodes]
            graph.add_edges_from(edges)

        return graph

    def __eq__(self, other) -> bool:
        if not isinstance(other, Graph):
            return False

        return (
            sorted(self.nodes) == sorted(other.nodes)
            and sorted(self.edges) == sorted(other.edges)
            and sorted(self.hyper_edges) == sorted(other.hyper_edges)
        )
