from model.edge import Edge, HyperEdge
from model.graph import Graph
from model.node import Node
from graphs.derive_base import derive_base
from production.p1 import p1
from production.p7 import p7

if __name__ == '__main__':
    g = derive_base()
    p7(g)
    p1(g)
    p7(g)
    g.draw_graph()
