import random
import time

def generate_random_graph(num_vertices, probability):
    graph = {}
    for i in range(num_vertices):
        neighbors = []
        for j in range(num_vertices):
            if i != j and random.random() < probability:
                neighbors.append(j)
        graph[i] = neighbors
    return graph

def greedy_coloring(graph):
    colors = {}  # Dicionário para armazenar as cores dos vértices

    # Função auxiliar para verificar se uma cor pode ser atribuída a um vértice
    def is_safe(node, color):
        for neighbor in graph[node]:
            if colors.get(neighbor) == color:
                return False
        return True

    # Percorre os vértices do grafo
    for node in graph:
        used_colors = set(colors.get(neighbor) for neighbor in graph[node] if neighbor in colors)
        # Encontra a menor cor não utilizada pelos vizinhos
        for color in range(len(graph)):
            if color not in used_colors and is_safe(node, color):
                colors[node] = color
                break

    return colors

# Exemplo de uso:
if __name__ == "__main__":
    num_vertices = 15000
    probability = 0.5
    # Gera uma matriz de adjacência aleatória
    graph = generate_random_graph(num_vertices, probability)
    print("Matriz de adjacência gerada:")
    for node, neighbors in graph.items():
        print(f"Vértice {node}: {neighbors}")

    # Mede o tempo de execução do algoritmo guloso
    start_time = time.time()
    coloring = greedy_coloring(graph)
    end_time = time.time()

    # Imprime os vértices com suas cores atribuídas
    print("\nColoração do grafo:")
    for node, color in coloring.items():
        print(f"Vértice {node} - Cor {color}")

    # Imprime a quantidade de cores utilizadas
    num_colors = len(set(coloring.values()))
    print("\nQuantidade de cores utilizadas:", num_colors)

    # Imprime o tempo de execução do algoritmo
    print("\nTempo de execução:", end_time - start_time, "segundos")
