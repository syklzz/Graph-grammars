from graphs.derive_base import derive_base
from production.p7 import p7
from production.p1 import p1
from production.p8 import p8
from production.p17 import p17
from production.p2 import p2
from production.p11 import p11
from production.p3 import p3

def derive():
    g = derive_base()
    g.draw_graph("01.png")
    p7(g)
    g.draw_graph("02.png")
    p1(g)
    g.draw_graph("03.png")
    p7(g, {8, 13, 10, 14})
    g.draw_graph("04.png")
    p8(g)
    g.draw_graph("05.png")
    p17(g)
    g.draw_graph("06.png")
    p2(g)
    print("p2")
    g.draw_graph("07.png")
    p11(g)
    g.draw_graph("08.png")
    print("p11")
    p1(g)
    print("p1")
    g.draw_graph("09.png")   
    p7(g, {8, 24, 23, 26})
    print("p7")
    g.draw_graph("10.png")
    p8(g)
    p8(g)
    print("p8")  #Check edge 17 19
    g.draw_graph("11.png")
    p2(g)
    g.draw_graph("12.png")
    print("p2")
    p3(g)   # Should divide id 17, 19, 8, 7
    g.draw_graph("13.png")
    print("p3")
    p1(g)  # Should divide 
    g.draw_graph("14.png")
    g.draw_graph()


if __name__ == '__main__':
    derive()
