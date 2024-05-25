import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4())  

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree_with_pause(graph, pos, fig, ax):
    ax.clear()
    colors = [node[1]['color'] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in graph.nodes(data=True)}
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, ax=ax)
    plt.pause(0.5)

def update_graph_colors(graph, tree_root):
    if tree_root is not None:
        graph.nodes[tree_root.id]['color'] = tree_root.color
        if tree_root.left:
            update_graph_colors(graph, tree_root.left)
        if tree_root.right:
            update_graph_colors(graph, tree_root.right)

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap(arr):
    nodes = [Node(key) for key in arr]
    
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    
    return nodes[0] if nodes else None

def generate_colors(n):
    colors = []
    for i in range(n):
        hue = i / n
        lightness = 0.5 + (0.5 * (i / n))
        rgb = colorsys.hls_to_rgb(hue, lightness, 1)
        colors.append('#%02x%02x%02x' % (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)))
    return colors

def dfs_visualize(node, colors, graph, pos, fig, ax, index=0):
    if node:
        node.color = colors[index]
        update_graph_colors(graph, node)
        draw_tree_with_pause(graph, pos, fig, ax)
        index += 1
        index = dfs_visualize(node.left, colors, graph, pos, fig, ax, index)
        index = dfs_visualize(node.right, colors, graph, pos, fig, ax, index)
    return index

def bfs_visualize(root, colors, graph, pos, fig, ax):
    queue = [(root, 0)]
    index = 0
    while queue:
        node, depth = queue.pop(0)
        if node:
            node.color = colors[index]
            update_graph_colors(graph, node)
            draw_tree_with_pause(graph, pos, fig, ax)
            index += 1
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]

heap_root = build_heap(arr)
colors = generate_colors(len(arr))


graph = nx.DiGraph()
pos = {heap_root.id: (0, 0)}
graph = add_edges(graph, heap_root, pos)


fig, ax = plt.subplots(figsize=(8, 5))
print("Обхід в глибину:")
dfs_visualize(heap_root, colors, graph, pos, fig, ax)
plt.show()

graph = nx.DiGraph()
pos = {heap_root.id: (0, 0)}
graph = add_edges(graph, heap_root, pos)

fig, ax = plt.subplots(figsize=(8, 5))
print("Обхід в ширину:")
bfs_visualize(heap_root, colors, graph, pos, fig, ax)
plt.show()

