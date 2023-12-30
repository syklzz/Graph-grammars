from model.edge import Label
from model.graph import Graph


def p16(graph: Graph) -> None:
    for hyper_edge in graph.hyper_edges:
        if hyper_edge.label == Label.P and len(hyper_edge.nodes) == 5 and hyper_edge.r == 0:
            hyper_edge.r = 1
            return
