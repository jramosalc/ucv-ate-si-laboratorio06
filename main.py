import heapq

# 1. Definición del grafo (Conexiones y costos reales g(n))
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Valores de la función heurística h(n) (Estimación al objetivo 'F')
heuristica = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

# 2. Implementación del algoritmo A*
def a_star(inicio, objetivo):
    # La cola de prioridad almacena tuplas: (prioridad_f, nodo_actual)
    cola = [(heuristica[inicio], inicio)] 
    visitados = set()
    costos = {inicio: 0}
    padres = {inicio: None}

    while cola:
        # Extrae el nodo con el menor valor de f(n)
        f_actual, actual = heapq.heappop(cola)

        if actual == objetivo:
            break

        if actual in visitados:
            continue
            
        visitados.add(actual)

        for vecino, costo in grafo[actual]:
            nuevo_costo = costos[actual] + costo # g(n)
            
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica[vecino] # f(n) = g(n) + h(n)
                heapq.heappush(cola, (prioridad, vecino))
                padres[vecino] = actual

    return padres, costos

# Función auxiliar para reconstruir y mostrar el camino de forma legible
def reconstruir_camino(padres, inicio, objetivo):
    camino = []
    actual = objetivo
    while actual is not None:
        camino.append(actual)
        actual = padres.get(actual)
    camino.reverse()
    return camino

# 3. Ejecutar la búsqueda
inicio_nodo = 'A'
objetivo_nodo = 'F'
diccionario_padres, diccionario_costos = a_star(inicio_nodo, objetivo_nodo)
camino_optimo = reconstruir_camino(diccionario_padres, inicio_nodo, objetivo_nodo)

print("--- RESULTADOS DEL ALGORITMO A* ---")
print(f"Diccionario de rutas (padres): {diccionario_padres}")
print(f"Camino óptimo encontrado: {' -> '.join(camino_optimo)}")
print(f"Costo total del camino g(n): {diccionario_costos[objetivo_nodo]}")