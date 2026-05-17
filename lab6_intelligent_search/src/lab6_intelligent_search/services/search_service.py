import networkx as nx
from lab6_intelligent_search.graph.graph_builder import build_graph
from lab6_intelligent_search.graph.heuristic import heuristics

def heuristic(node1, node2):
    return heuristics.get(node1, 0)

def find_route(start: str, goal: str):
    graph = build_graph()
    
    # Ejecuta el algoritmo A* usando NetworkX
    path = nx.astar_path(
        graph,
        start,
        goal,
        heuristic=heuristic,
        weight='weight'
    )
    cost = nx.path_weight(graph, path, weight='weight')
    
    return {
        'path': path,
        'cost': cost
    }