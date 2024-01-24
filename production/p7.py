from typing import Optional, List
from model.graph import Graph
from model.edge import Edge, Label


def p7(graph: Graph, ids: Optional[List[int]] = None) -> None:
    """
    Virtual adaptation: Marking the four-edged element to be broken.
    If a list of ids is provided, only hyperedges whose nodes' ids match the provided ids are considered.

    Parameters:
    graph (Graph): The graph on which the operation is performed.
    ids (List[int], optional): List of node ids to consider. If None, all nodes are considered. Defaults to None.
    """
    for hyper_edge in graph.hyper_edges:
        if ids is not None:
            if not all(node.id in ids for node in hyper_edge.nodes):
                continue
        if _should_break(hyper_edge):
            hyper_edge.r = 1
            return


def _should_break(edge: Edge) -> bool:
    return edge.label == Label.Q and len(edge.nodes) == 4 and edge.r == 0
