from model.edge import Edge, HyperEdge, Label
from model.graph import Graph
from model.node import Node
from production.p3 import p3


def exact_left_side():
    """
    Graph that exactly matches the left side of p7 production
    Given on slide number 16.
    
    Slide 12
    """
    g = Graph()
    
    n1 = Node(0, 0, 0)
    n2 = Node(2, 0, 0)
    n3 = Node(2, 2, 0)
    n4 = Node(0, 2, 0)
    
    n5 = Node(2, 1, 1)
    n6 = Node(1, 0, 1)
    
    g.add_nodes([n1, n2, n3, n4, n5, n6])
    
    g.add_edge(Edge(n1, n6, 0))
    g.add_edge(Edge(n6, n2, 0))
    g.add_edge(Edge(n2, n5, 0))
    g.add_edge(Edge(n5, n3, 0))
    g.add_edge(Edge(n3, n4, 0))
    g.add_edge(Edge(n4, n1, 0))
    
    g.add_hyper_edge(HyperEdge([n1, n2, n3, n4], 1, Label.Q))    
    
    return g

def complex_graph_with_match():
    """
    A square with a pentagon attached to it.
    Hanging nodes in between the square.
    
    1 - 2 - 5
    |   |    \
    | Q 8  P  6
    |   |    /
    4-9-3 - 7
    """
    graph = Graph()

    node1 = Node(0, 2, 0)
    node2 = Node(2, 2, 0)
    node3 = Node(2, 0, 0)
    node4 = Node(0, 0, 0)

    node5 = Node(4, 2, 0)
    node6 = Node(5, 1, 0)
    node7 = Node(4, 0, 0)

    node8 = Node(2, 1, 1)
    node9 = Node(1, 0, 1)

    graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8, node9])

    graph.add_edge(Edge(node1, node2, "B1"))
    graph.add_edge(Edge(node8, node2, "B2"))
    graph.add_edge(Edge(node8, node3, "B2"))
    graph.add_edge(Edge(node4, node9, "B3"))
    graph.add_edge(Edge(node3, node9, "B3"))
    graph.add_edge(Edge(node4, node1, "B4"))

    graph.add_edge(Edge(node2, node5, "B5"))
    graph.add_edge(Edge(node5, node6, "B6"))
    graph.add_edge(Edge(node6, node7, "B7"))
    graph.add_edge(Edge(node7, node3, "B8"))
    
    graph.add_hyper_edge(HyperEdge([node1, node2, node3, node4], 1, Label.Q))
    graph.add_hyper_edge(HyperEdge([node2, node3, node5, node6, node7], 1, Label.P))
    return graph
    
    


def graph_with_no_match():
    """
    A square with a pentagon attached to it.
    Hanging nodes in between the square.
    Node 1 removed.
    
        2 - 5
        |    \
        8  P  6
        |    /
    4-9-3 - 7
    """
    graph = Graph()

    node2 = Node(2, 2, 0)
    node3 = Node(2, 0, 0)
    node4 = Node(0, 0, 0)

    node5 = Node(4, 2, 0)
    node6 = Node(5, 1, 0)
    node7 = Node(4, 0, 0)

    node8 = Node(2, 1, 1)
    node9 = Node(1, 0, 1)

    graph.add_nodes([ node2, node3, node4, node5, node6, node7, node8, node9])

    graph.add_edge(Edge(node8, node2, "B2"))
    graph.add_edge(Edge(node8, node3, "B2"))
    graph.add_edge(Edge(node4, node9, "B3"))
    graph.add_edge(Edge(node3, node9, "B3"))

    graph.add_edge(Edge(node2, node5, "B5"))
    graph.add_edge(Edge(node5, node6, "B6"))
    graph.add_edge(Edge(node6, node7, "B7"))
    graph.add_edge(Edge(node7, node3, "B8"))
    
    graph.add_hyper_edge(HyperEdge([node2, node3, node5, node6, node7], 1, Label.P))
    return graph

def graph_wrong_label():
    """
    Graph with wrong label on hyper edge.
    """
    wrong_label = Label.P
     
    g = Graph()
    
    n1 = Node(0, 0, 0)
    n2 = Node(2, 0, 0)
    n3 = Node(2, 2, 0)
    n4 = Node(0, 2, 0)
    
    n5 = Node(2, 1, 1)
    n6 = Node(1, 0, 1)
    
    g.add_nodes([n1, n2, n3, n4, n5, n6])
    
    g.add_edge(Edge(n1, n6, 0))
    g.add_edge(Edge(n6, n2, 0))
    g.add_edge(Edge(n2, n5, 0))
    g.add_edge(Edge(n5, n3, 0))
    g.add_edge(Edge(n3, n4, 0))
    g.add_edge(Edge(n4, n1, 0))
    
    g.add_hyper_edge(HyperEdge([n1, n2, n3, n4], 1, wrong_label))    
    
    return g


def graph_wrong_hanging_node():
    """
    Graph with one hanging node not being a hanging node.
    """
    
    wrong_hanging_node = 0
     
    g = Graph()
    
    n1 = Node(0, 0, 0)
    n2 = Node(2, 0, 0)
    n3 = Node(2, 2, 0)
    n4 = Node(0, 2, 0)
    
    n5 = Node(2, 1, 1)
    n6 = Node(1, 0, wrong_hanging_node)
    
    g.add_nodes([n1, n2, n3, n4, n5, n6])
    
    g.add_edge(Edge(n1, n6, 0))
    g.add_edge(Edge(n6, n2, 0))
    g.add_edge(Edge(n2, n5, 0))
    g.add_edge(Edge(n5, n3, 0))
    g.add_edge(Edge(n3, n4, 0))
    g.add_edge(Edge(n4, n1, 0))
    
    g.add_hyper_edge(HyperEdge([n1, n2, n3, n4], 1, Label.Q))    
    
    return g
    

def graph_wrong_r():
    """
    Graph with Q not having the r argument equal to 1.
    """
    wrong_r = 0
    
    g = Graph()
    
    n1 = Node(0, 0, 0)
    n2 = Node(2, 0, 0)
    n3 = Node(2, 2, 0)
    n4 = Node(0, 2, 0)
    
    n5 = Node(2, 1, 1)
    n6 = Node(1, 0, 1)
    
    g.add_nodes([n1, n2, n3, n4, n5, n6])
    
    g.add_edge(Edge(n1, n6, 0))
    g.add_edge(Edge(n6, n2, 0))
    g.add_edge(Edge(n2, n5, 0))
    g.add_edge(Edge(n5, n3, 0))
    g.add_edge(Edge(n3, n4, 0))
    g.add_edge(Edge(n4, n1, 0))
    
    g.add_hyper_edge(HyperEdge([n1, n2, n3, n4], wrong_r, Label.Q))    
    
    return g
    

if __name__=="__main__":
    print("This module is not meant to be executed directly.")
    print("But if you insist, here is a demo:")
    
    for graph in [exact_left_side(), complex_graph_with_match(), graph_with_no_match(), graph_wrong_label(), graph_wrong_hanging_node(), graph_wrong_r()]:
        graph.draw_graph()
        p3(graph)
        graph.draw_graph()
