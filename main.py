from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node
from production.p16 import p16
from production.p2 import p2
from production.p8 import p8
from production.p9 import p9


def make_ex2_graph():
    g = Graph()

    # ramka czworokata
    node1 = Node(0, 0, 0)
    node2 = Node(4, 0, 0)
    node3 = Node(4, 4, 0)
    node4 = Node(0, 4, 0)
    g.add_nodes([node1, node2, node3, node4])

    g.add_edge(Edge(node1, node2, 0))
    g.add_edge(Edge(node3, node4, 0))
    g.add_edge(Edge(node4, node1, 0))

    # pieciokat w srodku
    node5 = Node(1, 1, 0)
    node6 = Node(2, 1, 0)
    node7 = Node(3, 2, 0)
    node8 = Node(2, 3, 0)
    node9 = Node(1, 3, 0)
    g.add_nodes([node5, node6, node7, node8, node9])

    g.add_edge(Edge(node5, node6, 0))
    g.add_edge(Edge(node6, node7, 0))
    g.add_edge(Edge(node7, node8, 0))
    g.add_edge(Edge(node8, node9, 0))
    g.add_edge(Edge(node9, node5, 0))

    # ekstra node w czworokacie
    node10 = Node(4, 2, 0)
    g.add_node(node10)
    g.add_edge(Edge(node7, node10, 0))

    # laczenie dwoch figur
    g.add_edge(Edge(node1, node5, 0))
    g.add_edge(Edge(node4, node9, 0))
    g.add_edge(Edge(node8, node3, 0))
    # g.add_edge(Edge(node8, node3, 0))
    g.add_edge(Edge(node6, node2, 0))
    g.add_edge(Edge(node2, node10, 0))
    g.add_edge(Edge(node3, node10, 0))
    

    # dodawanie hiperkrawedzi - na razie wszystkie nieoznaczone do łamania
    g.add_hyper_edge(HyperEdge([node1, node5, node9, node4], 0, Label.Q))
    g.add_hyper_edge(HyperEdge([node4, node9, node3, node8], 0, Label.Q))
    g.add_hyper_edge(HyperEdge([node1, node2, node6, node5], 0, Label.Q))
    g.add_hyper_edge(HyperEdge([node2, node10, node7, node6], 0, Label.Q))
    g.add_hyper_edge(HyperEdge([node10, node7, node8, node3], 0, Label.Q))

    g.add_hyper_edge(HyperEdge([node5, node6, node7, node8, node9], 0, Label.P))

    return g

def find_hyper_edges_with_label_and_ids(graph: Graph, label: Label, ids: list[int]):
    for hyper_edge in graph.hyper_edges:
        if hyper_edge.label == label:
            nodes = list(filter(lambda x: x.id in ids,hyper_edge.nodes))
            if len(nodes) == len(ids):
                return hyper_edge


if __name__ == '__main__':
    graph: Graph = make_ex2_graph()

    p16(graph)
    p9(graph)
    hyper_edge = find_hyper_edges_with_label_and_ids(graph, Label.Q, [10, 13, 6, 12])
    hyper_edge.r = 1

    graph.draw_graph()
    p8(graph)
    p8(graph)
    graph.draw_graph()

    p2(graph)
    graph.draw_graph()


    # [bug with P8]
    # line 21, in p8
    #   if mid_node.h == 1:
    # AttributeError: 'NoneType' object has no attribute 'h'
    hyper_edge = find_hyper_edges_with_label_and_ids(graph, Label.Q, [])


    # graph.draw_graph()
