from model.graph import Graph
from model.edge import HyperEdge, Edge, Label


def p7(graph: Graph, chosen_ids: set = None) -> None:
    """
    Virtual adaptation: Marking the four-edged element to be broken
    """
    for hyper_edge in graph.hyper_edges:
        if _should_break(hyper_edge) and (chosen_ids is None or _has_chosen_ids(hyper_edge, chosen_ids)):
            hyper_edge.r = 1
            return
        
def _should_break(edge: Edge) -> bool:
    return edge.label == Label.Q and len(edge.nodes) == 4 and edge.r == 0

def _has_chosen_ids(hyper_edge: HyperEdge, chosen_ids: set[int]):
    hyper_edge_nodes = {node.id for node in hyper_edge.nodes}
    return chosen_ids == hyper_edge_nodes
