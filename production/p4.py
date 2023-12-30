from model.graph import Graph
from model.node import Node
from model.edge import Label, HyperEdge, Edge
from itertools import combinations
import networkx as nx

from utils.common import calculate_y, calculate_x


def p4(graph: Graph) -> None:
    for hyper_edge in graph.hyper_edges:
        if hyper_edge.r == 1 and hyper_edge.label == Label.Q and check_if_all_nodes_h_0(hyper_edge.nodes):
            neighbours_h1 = {}

            # finding all nodes with h1 that are neighbours to considered node
            for node in hyper_edge.nodes:
                neighbours = h1_neighbours_for_node(node, graph)
                neighbours_h1[node] = neighbours

            common_h1_neighbours = []
            for node1, node2 in combinations(hyper_edge.nodes, 2):
                common_neighbours = list(set(neighbours_h1[node1]) & set(neighbours_h1[node2]))
                if len(common_neighbours) == 1:
                    common_h1_neighbours.append((node1, node2, common_neighbours[0]))

            # apply production only for 2 nodes with h==1
            edges_without_hanging_nodes = []

            if len(common_h1_neighbours) == 2:
                for node1, node2 in combinations(hyper_edge.nodes, 2):
                    edge = does_edge_exist(node1, node2, graph)
                    if edge is not None:
                        edges_without_hanging_nodes.append(edge)

            new_nodes = []
            if len(edges_without_hanging_nodes) == 2:
                # add missing new nodes
                for edge in edges_without_hanging_nodes:
                    graph.edges.remove(edge)
                    new_node = Node(calculate_x([edge.n1, edge.n2]), calculate_y([edge.n1, edge.n2]), edge.b)
                    new_nodes.append(new_node)
                    graph.add_node(new_node)
                    edge1 = Edge(edge.n1, new_node, edge.b)
                    edge2 = Edge(edge.n2, new_node, edge.b)
                    graph.add_edge(edge1)
                    graph.add_edge(edge2)

                # apply central point of production
                graph.hyper_edges.remove(hyper_edge)
                central_node = Node(calculate_x(hyper_edge.nodes), calculate_y(hyper_edge.nodes), 0)
                graph.add_node(central_node)

                graph.add_edge(Edge(central_node, new_nodes[0], 0))
                graph.add_edge(Edge(central_node, new_nodes[1], 0))
                graph.add_edge(Edge(central_node, common_h1_neighbours[0][2], 0))
                graph.add_edge(Edge(central_node, common_h1_neighbours[1][2], 0))

                # create small productions and hyper-edges
                original_h1_nodes: list[Node] = list(map(lambda x: x[2], common_h1_neighbours))

                for node in hyper_edge.nodes:
                    nodes_for_hyper_edge = find_nodes_for_hyper_edge(node, original_h1_nodes, new_nodes, graph)
                    nodes_for_hyper_edge.append(central_node)

                    new_hyper_edge = HyperEdge(nodes_for_hyper_edge, 0, Label.Q)
                    graph.add_hyper_edge(new_hyper_edge)

                for old_h1 in original_h1_nodes:
                    old_h1.h = 0


def find_nodes_for_hyper_edge(node: Node, h1_nodes: list[Node], new_nodes: list[Node], graph: Graph):
    result = [node]
    for h1_node in h1_nodes:
        edge = does_edge_exist(node, h1_node, graph)
        if edge is not None:
            result.append(h1_node)
    for new_node in new_nodes:
        edge = does_edge_exist(node, new_node, graph)
        if edge is not None:
            result.append(new_node)
    return result

def does_edge_exist(node1: Node, node2: Node, graph: Graph) -> Edge | None:
    for edge in graph.edges:
        if (edge.n1 == node1 and edge.n2 == node2) or (edge.n1 == node2 and edge.n2 == node1):
            return edge
    return None


def check_if_all_nodes_h_0(nodes: list[Node]) -> bool:
    for node in nodes:
        if node.h != 0:
            return False
    return True


def h1_neighbours_for_node(node: Node, graph: Graph) -> list[Node]:
    h1_neighbours = []
    for edge in graph.edges:
        if edge.n1 == node:
            if edge.n2.h == 1:
                h1_neighbours.append(edge.n2)
            pass
        elif edge.n2 == node:
            if edge.n2 == node:
                if edge.n1.h == 1:
                    h1_neighbours.append(edge.n1)

    return h1_neighbours
