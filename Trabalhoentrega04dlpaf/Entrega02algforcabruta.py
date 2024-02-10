import numpy as np
import time

def gerar_grafo(n):
    adjacency_matrix = np.random.randint(0, 2, (n, n))
    return adjacency_matrix

def printConfiguration(colorArray):
    for i, color in enumerate(colorArray):
        print(f"Vertice {i+1} alocado na cor {color}")

def isSafe(graph, colorArray):
    n = len(graph)
    for i in range(n):
        for j in range(i + 1, n):   
            if graph[i][j] == 1 and colorArray[i] == colorArray[j]:
                return False
    return True

def graphColoringAlgorithm(graph, m, i, colorArray):
    global color
    global colorArrayPrint

    if i == len(graph):
        if isSafe(graph, colorArray):
            colorArrayPrint = colorArray.copy()
            color = len(set(colorArray))
            return True
        return False

    for j in range(1, m + 1):
        colorArray[i] = j
        if graphColoringAlgorithm(graph, m, i + 1, colorArray):
            return True
        colorArray[i] = 0

    return False

def main():
    n = 9  # Define o número de vértices no grafo
    graph = gerar_grafo(n)
    
    print("Matriz de Adjacência:")
    print(graph)

    colors = list(range(1, n + 1))  # Lista de cores disponíveis
    iterations = 10

    for _ in range(iterations):
        start_time = time.time()
        colorArray = [0] * n
        if graphColoringAlgorithm(graph, n, 0, colorArray):
            end_time = time.time()
            print("\nColoração válida encontrada:")
            printConfiguration(colorArrayPrint)
            print("Número de cores utilizadas:", color)
            print("Tempo de execução: {:.8f} segundos".format(end_time - start_time))
            break
        else:
            print("\nNão foi possível colorir o grafo.")

if __name__ == "__main__":
    main()
