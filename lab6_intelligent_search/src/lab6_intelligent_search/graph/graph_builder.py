import networkx as nx

def build_graph():
    graph = nx.Graph()
    # Construcción del mapa urbano con costos reales g(n)
    graph.add_weighted_edges_from([
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'D', 2),
        ('B', 'E', 5),
        ('C', 'F', 3),
        ('E', 'F', 1)
    ])
    return graph