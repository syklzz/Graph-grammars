def calculate_x(nodes):
    return sum(list(map(lambda node: node.x, nodes))) / len(nodes)


def calculate_y(nodes):
    return sum(list(map(lambda node: node.y, nodes))) / len(nodes)


def map_edges_to_ids(edges):
    return list(map(lambda edge: (edge.n1.id, edge.n2.id), edges))


def map_nodes_to_ids(nodes):
    return list(map(lambda node: node.id, nodes))
