# Завдання 5. Візуалізація обходу бінарного дерева

import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#B0C4DE"  # початковий колір
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(root, title="Tree Visualization"):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, font_color='black')
    plt.show()


def generate_color_gradient(n):
    """Генерує n відтінків кольору від темного до світлого (від #0000AA до #99CCFF)"""
    gradient = []
    for i in range(n):
        ratio = i / max(n - 1, 1)
        r = int(18 + (153 - 18) * ratio)
        g = int(30 + (204 - 30) * ratio)
        b = int(240 + (255 - 240) * ratio)
        color = f'#{r:02X}{g:02X}{b:02X}'
        gradient.append(color)
    return gradient


def bfs_color(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    colors = generate_color_gradient(len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i]


def dfs_color(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # правий спочатку — лівий вгорі при pop
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    colors = generate_color_gradient(len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i]


# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# BFS обход
bfs_color(root)
draw_tree(root, title="BFS: Обхід у ширину")

# Скидання кольорів
for node in [root, root.left, root.right, root.left.left,
             root.left.right, root.right.left, root.right.right]:
    node.color = "#B0C4DE"

# DFS обход
dfs_color(root)
draw_tree(root, title="DFS: Обхід у глибину")
