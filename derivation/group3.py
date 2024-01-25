# from graphs import derive_base
from graphs.derive_base import derive_base

from production.p1 import p1
from production.p10 import p10
from production.p2 import p2

from production.p3 import p3
from production.p7 import p7
from production.p8 import p8
from production.p17 import p17
from model.node import Node
from model.edge import Edge, HyperEdge, Label


def derive():
    g = derive_base()

    g.draw_graph("d3-0-init.png")
    p7(g)
    g.draw_graph("d3-1-p7.png")
    p1(g)
    g.draw_graph("d3-2-p1.png")
    p7(g, [8, 10, 14, 13])
    g.draw_graph("d3-3-p7.png")
    p8(g)
    g.draw_graph("d3-4-p8.png")
    # Bug with P17: renames nodes
    p17(g)
    g.draw_graph("d3-5-p17.png")
    p10(g)

    # ### ARTIFICIAL P3 PRODUCTION ###
    g.hyper_edges.pop(2)
    middle_node = Node(2.85, 5.25, 0)
    g.add_node(middle_node)
    g.add_edge(Edge(middle_node, g.nodes[19], 0))
    g.nodes[19].h = 0
    g.add_edge(Edge(middle_node, g.nodes[14], 0))
    g.nodes[14].h = 0

    g.add_hyper_edge(
        HyperEdge([g.nodes[20], g.nodes[19], g.nodes[8], g.nodes[14]], 0, Label.Q))
    g.draw_graph("d3-7-p3.png")

    # p3(g)  # Bug with p3: circular import and does not work/end
    # g.draw_graph("d3-7-p3.png")

    # ### END ARTIFICIAL P3 PRODUCTION ###

    p1(g)
    g.draw_graph("d3-9-p1.png")
    p7(g, [8, 24, 21, 22])
    g.draw_graph("d3-10-p7.png")
    p8(g, [8, 14, 19, 20])
    g.draw_graph("d3-11-p8.png")
    p8(g, [8, 13, 15, 19])
    g.draw_graph("d3-12-p8.png")
    # p2(g)
    # g.draw_graph("d3-13-p2.png")


if __name__ == "__main__":
    derive()
