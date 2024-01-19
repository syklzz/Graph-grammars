from graphs.derive_base import derive_base
from production.p7 import p7
from production.p1 import p1
from production.p8 import p8
from production.p17 import p17
from production.p2 import p2
# from production.p11 import p11
# from production.p3 import p3

def derive():
    g = derive_base()
    g.draw_graph()
    p7(g)
    g.draw_graph()
    p1(g)
    g.draw_graph()
    p7(g, {8, 13, 10, 14})
    g.draw_graph()
    p8(g)
    g.draw_graph()
    p17(g)
    g.draw_graph()
    p2(g)
    g.draw_graph()


if __name__ == '__main__':
<<<<<<< HEAD
    derive()
=======
    derive()
>>>>>>> 93b0dcf (d2 start)
