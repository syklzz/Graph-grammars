def calculate_x(nodes):
    return sum(list(map(lambda node: node.x, nodes))) / len(nodes)


def calculate_y(nodes):
    return sum(list(map(lambda node: node.y, nodes))) / len(nodes)
