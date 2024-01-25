from itertools import combinations
from statistics import mean
import networkx as nx

from model.edge import Edge, HyperEdge, Label
from model.graph import Graph

from typing import List, NamedTuple, Set

from model.node import Node


class Subgraph(NamedTuple):
    hyper_edge: HyperEdge
    nodes: Set[Node]
    edges: List[Edge]
    
class SimpleEdge(NamedTuple):
    n1_id: int
    n2_id: int


def p3(graph: Graph) -> None:
    """
    Breaking the four-edged element if it is marked and has two hanging nodes
    """
    subgraph = _find_isomorphic_subgraph(graph)
    if subgraph is not None:
        _apply_production(graph, subgraph)
        
        
def _find_isomorphic_subgraph(graph: Graph) -> Subgraph | None:
    valid_hyper_edges: List[HyperEdge] = [
        hyper_edge
        for hyper_edge in graph.hyper_edges
        if hyper_edge.label == Label.Q
        and len(hyper_edge.nodes) == 4 
        and hyper_edge.r == 1 
        and all(node.h == 0 for node in hyper_edge.nodes)
    ]
    
    # print("Found valid hyper edges:", valid_hyper_edges)
    subgraphs = (
            Subgraph(hyper_edge, _get_nodes_from_edges(edges), edges)
            for hyper_edge in valid_hyper_edges
            for edges in _get_valid_edges(graph, hyper_edge.nodes)
            if _validate_subgraph(edges, hyper_edge.nodes)
    ) 
    return next(subgraphs, None)
        

def _get_valid_edges(graph: Graph, corner_nodes: List[Node]) -> List[Edge]:
    simple_edges = _edges_to_simple_edges(graph.edges) 
       
    corner_edges = [_get_edge(simple_edges, corner_node1, corner_node2) 
                    for corner_node1 in corner_nodes
                    for corner_node2 in corner_nodes
                    if corner_node1.id > corner_node2.id 
                    and _does_edge_exist(simple_edges, corner_node1, corner_node2)]
    
    if len(corner_edges) != 2:
        return [] 
    
    count_nodes = {node: 0 for node in corner_nodes}
    for edge in corner_edges:
        count_nodes[edge.n1] += 1
        count_nodes[edge.n2] += 1
    
    nodes_with_one_edge_found = [node for node, count in count_nodes.items() if count == 1]
    if len(nodes_with_one_edge_found) != 2:
        return []
    
    nodes_without_edge_found = [node for node, count in count_nodes.items() if count == 0]
    if len(nodes_without_edge_found) != 1:
        return []
        
    n_a = nodes_without_edge_found[0]
    n_b1, n_b2 = tuple(nodes_with_one_edge_found)
    
    hanging_nodes = [n_h for n_h in _get_hanging_nodes(graph.nodes) if _does_edge_exist(simple_edges, n_h, n_a)]
    # valid_combinations = [combination for combination in combinations(hanging_nodes, 2) 
    #                       if _does_edge_exist(simple_edges, combination[0], n_b1) or _does_edge_exist(simple_edges, combination[0], n_b2)]
    hanging_node_edges = []
    for n_h in hanging_nodes:
        hanging_node_edges.append(_get_edge(simple_edges, n_h, n_a))
        if _does_edge_exist(simple_edges, n_h, n_b1):
            hanging_node_edges.append(_get_edge(simple_edges, n_h, n_b1))
        elif _does_edge_exist(simple_edges, n_h, n_b2):
            hanging_node_edges.append(_get_edge(simple_edges, n_h, n_b2))
        
    return [corner_edges + hanging_node_edges]


def _edges_to_simple_edges(edges: List[Edge]) -> dict[SimpleEdge, Edge]:
    return {SimpleEdge(edge.n1.id, edge.n2.id): edge for edge in edges}

def _does_edge_exist(edges: dict[SimpleEdge, Edge], n1: Node, n2: Node) -> bool:
    return SimpleEdge(n1.id, n2.id) in edges or SimpleEdge(n2.id, n1.id) in edges

def _get_edge(edges: dict[SimpleEdge, Edge], n1: Node, n2: Node) -> Edge:
    return edges[SimpleEdge(n1.id, n2.id)] if SimpleEdge(n1.id, n2.id) in edges else edges[SimpleEdge(n2.id, n1.id)]

def _get_hanging_nodes(nodes: list[Node]) -> list[Node]:
    return [node for node in nodes if node.h == 1]

def _validate_subgraph(edges: List[Edge], corner_nodes: List[Node]) -> bool:
    edge_nodes = _get_nodes_from_edges(edges)
    hanging_nodes = list(edge_nodes - set(corner_nodes))
    
    are_nodes_in_edges = _validate_nodes_in_edges(edge_nodes, corner_nodes)
    are_hanging_nodes_valid = _validate_hanging_nodes(hanging_nodes)
    
    base_graph = _create_base_graph()
    subgraph = _create_subgraph(edges, corner_nodes)
    is_isomorphic = nx.is_isomorphic(base_graph, subgraph)
    
    return are_nodes_in_edges and are_hanging_nodes_valid and is_isomorphic


def _create_base_graph() -> nx.Graph:
    """Graph with four-edged element and a hyperEdge with label Q in the middle.
    The left side of P3 production. Given on slide number 12.
    
    "corner" nodes: 1,2,3,4
    "hanging" nodes: 5,6
    
    """
    corner_and_hanging_nodes_edge_list = [(1, 6), (6, 2), (2, 5), (5, 3), (3, 4), (4, 1)]
    hyper_edge_edge_list = [(0, 1), (0, 2), (0, 3), (0, 4)]
    
    return nx.Graph(corner_and_hanging_nodes_edge_list + hyper_edge_edge_list)
    
    
def _create_subgraph(edges: List[Edge], nodes: List[Node]) -> nx.Graph:
    """Creates a subgraph from the given edges.
    
    arguments:
    edges -- list of edges (label E)
    nodes -- list of nodes connected with a hyperEdge with label Q
    
    returns:
    nx.Graph object with edges and nodes from the arguments
    """
    ARBITRARY_HYPER_EDGE_ID = -1
    
    corner_and_hanging_nodes_edge_list = [(edge.n1.id, edge.n2.id) for edge in edges]
    hyper_edge_edge_list = [(ARBITRARY_HYPER_EDGE_ID, node.id) for node in nodes]
    
    return nx.Graph(corner_and_hanging_nodes_edge_list + hyper_edge_edge_list)

def _validate_nodes_in_edges(edge_nodes: List[Node], nodes: List[Node]) -> bool:
    edge_node_ids = set(edge_node.id for edge_node in edge_nodes)
    return all(node.id in edge_node_ids for node in nodes)

def _validate_hanging_nodes(hanging_nodes: List[Node]) -> bool:
    only_two_hanging_nodes = len(hanging_nodes) == 2
    hanging_nodes_have_h_1 = all(node.h == 1 for node in hanging_nodes)
    return only_two_hanging_nodes and hanging_nodes_have_h_1
    
def _apply_production(graph: Graph, subgraph: Subgraph) -> None:
    """Applies the production P3 to the graph.
    
    
    arguments:
    graph -- graph to which the production is applied
    subgraph -- subgraph of the graph that is isomorphic to the left side of the production
    """

    hyper_edge, nodes, edges = subgraph
    graph.hyper_edges.remove(hyper_edge)
    
    old_hanging_nodes = [node for node in nodes if node.h == 1]
    old_outer_edges = [edge for edge in edges if edge.n1 in old_hanging_nodes or edge.n2 in old_hanging_nodes]
    edges_to_change = [edge for edge in edges if edge.n1.h == 0 and edge.n2.h == 0]

    middle_node = _create_derived_node(hyper_edge.nodes, 0)
    new_hanging_nodes = [_create_derived_node([edge.n1, edge.n2], int(not edge.b))
                         for edge in edges_to_change]
    _remove_edges_from_graph(graph, edges_to_change)
    _add_nodes_to_graph(graph, [middle_node] + new_hanging_nodes)    

    new_outer_edges = [outer_edge 
                       for edge, h_node in zip(edges_to_change, new_hanging_nodes)
                       for outer_edge in 
                        (Edge(n1=edge.n1, n2=h_node, b=edge.b),
                         Edge(n1=h_node, n2=edge.n2, b=edge.b))]
    new_inner_edges = [Edge(n1=middle_node, n2=h_node, b=0)
                       for h_node in (old_hanging_nodes + new_hanging_nodes)]
    _add_edges_to_graph(graph, new_outer_edges + new_inner_edges)

    all_subgraph_outer_edges = new_outer_edges + old_outer_edges
    new_hyper_edges = [HyperEdge(
        nodes=([node, middle_node] +
               _find_adjoining_nodes(node, all_subgraph_outer_edges)),
        r=0,
        label=Label.Q,
        ) for node in hyper_edge.nodes]    
    _add_hyper_edges_to_graph(graph, new_hyper_edges)

    for hanging_node in old_hanging_nodes:
        hanging_node.h = 0
    

def _create_derived_node(nodes: List[Node], h: int) -> Node:
    return Node(
        x=mean(n.x for n in nodes),
        y=mean(n.y for n in nodes),
        h=h,
    )

def _add_nodes_to_graph(graph: Graph, nodes: List[Node]) -> None:
    for node in nodes:
        graph.add_node(node)
        
def _add_edges_to_graph(graph: Graph, edges: List[Edge]) -> None:
    for edge in edges:
        graph.add_edge(edge)

def _add_hyper_edges_to_graph(graph: Graph, hyper_edges: List[HyperEdge]) -> None:
    for e in hyper_edges:
        graph.add_hyper_edge(e)
        
def _remove_edges_from_graph(graph: Graph, edges: List[Edge]) -> None:
    for edge in edges:
        graph.edges.remove(edge)


def _find_adjoining_nodes(node: Node, edges: List[Edge]) -> List[Node]:
    return [edge.n1 if edge.n2 == node else edge.n2 for edge in edges if node in (edge.n1, edge.n2)]
    
def _get_nodes_from_edges(edges: List[Edge]) -> Set[Node]:
    return set([edge.n1 for edge in edges] + [edge.n2 for edge in edges])