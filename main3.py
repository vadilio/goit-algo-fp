# Завдання 3. Дерева, алгоритм Дейкстри
# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у
# зваженому графі, використовуючи бінарну купу. Завдання включає
# створення графа, використання піраміди для оптимізації вибору
# вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(heap, (distance, neighbor))
    return distances, previous


def reconstruct_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    if path[0] == start:
        return path
    return []


def draw_graph(graph, distances, previous, start):
    G = nx.Graph()

    # Добавляем ребра
    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)  # Расположение вершин

    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Рисуем все ребра с весами серым цветом
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_color='red')

    # Подсвечиваем кратчайшие пути от start ко всем вершинам
    for target in graph:
        if target == start:
            continue
        path = reconstruct_path(previous, start, target)
        if len(path) > 1:
            edges_in_path = list(zip(path[:-1], path[1:]))
            nx.draw_networkx_edges(
                G, pos,
                edgelist=edges_in_path,
                width=4,
                edge_color='green'
            )

    plt.title(f"Граф с кратчайшими путями от вершины '{start}'")
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    graph = {
        'A': [('B', 5), ('C', 1)],
        'B': [('A', 5), ('C', 2), ('D', 1)],
        'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
        'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
        'E': [('C', 8), ('D', 3)],
        'F': [('D', 6)]
    }

    start_vertex = 'A'
    distances, previous = dijkstra(graph, start_vertex)

    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"  До {vertex}: {distance}")

    draw_graph(graph, distances, previous, start_vertex)
