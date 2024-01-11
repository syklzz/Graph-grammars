from model.graph import Graph
from model.edge import Edge, Label


def p7(graph: Graph) -> None:
    """
    Virtual adaptation: Marking the four-edged element to be broken
    """
    for hyper_edge in graph.hyper_edges:
        if _should_break(hyper_edge):
            hyper_edge.r = 1
            return
        
def _should_break(edge: Edge) -> bool:
    return edge.label == Label.Q and len(edge.nodes) == 4 and edge.r == 0