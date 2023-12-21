class Node:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h
        self.id = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, Node):
            return False

        return self.x == other.x and self.y == other.y and self.h == other.h

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.h, self.id))

    def __repr__(self) -> str:
        return str(self.__dict__)
    
    def __lt__(self, other) -> bool:
        return (self.x, self.y, self.h) < (other.x, other.y, other.h)
