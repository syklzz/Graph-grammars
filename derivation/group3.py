from graphs import derive_base
from graphs.derive_base import derive_base
from production.p1 import p1
from production.p7 import p7

def derive():
    g = derive_base()
    p7(g)
    p1(g)
    p7(g, [9, 12, 15, 16])
    g.draw_graph()


if __name__ == '__main__':
    derive()