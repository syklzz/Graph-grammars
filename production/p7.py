from typing import Optional, Tuple
from model.graph import Graph
from model.edge import Edge, Label


def p7(graph: Graph, coordinates: Optional[Tuple[int, int, int]] = None) -> None:
    """
    Virtual adaptation: Marking the four-edged element to be broken
    """
    for hyper_edge in graph.hyper_edges:
        if coordinates is not None:
            if not any(node.x == coordinates[0] and node.y == coordinates[1] and node.h == coordinates[2] for node in hyper_edge.nodes):
                continue
        if _should_break(hyper_edge):
            hyper_edge.r = 1
            return


def _should_break(edge: Edge) -> bool:
    return edge.label == Label.Q and len(edge.nodes) == 4 and edge.r == 0
