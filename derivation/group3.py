# from graphs import derive_base
from graphs.derive_base import derive_base

from production.p1 import p1
from production.p10 import p10

from production.p3 import p3
from production.p7 import p7
from production.p8 import p8
from production.p17 import p17


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
    g.draw_graph("d3-6-p10.png")
    p3(g)  # Bug with p3: circular import and does not work/end
    g.draw_graph("d3-7-p3.png")


if __name__ == "__main__":
    derive()
