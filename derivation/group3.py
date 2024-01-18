from graphs import derive_base
from graphs.derive_base import derive_base
from production.p1 import p1
from production.p10 import p10
# from production.p3 import p3
from production.p7 import p7
from production.p8 import p8
from production.p17 import p17

def derive():
    g = derive_base()
    # g.draw_graph()
    p7(g)
    # g.draw_graph()
    p1(g)
    # g.draw_graph()
    p7(g, [8, 10, 14, 13])
    # g.draw_graph()
    p8(g)
    g.draw_graph()
    p17(g)  # Bug with P17: renames nodes
    g.draw_graph()
    p10(g)
    g.draw_graph()
    # p3(g)  # Bug with p3: circular import and does not work/end
    # g.draw_graph()


if __name__ == '__main__':
    derive()
