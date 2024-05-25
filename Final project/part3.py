import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance)) 
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance  

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    
    priority_queue = [(0, initial)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)


        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight
            if neighbor not in visited or distance < visited[neighbor]:
                visited[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                path[neighbor] = current_node

    return visited, path

def visualize_graph(graph, paths, initial_node):
    G = nx.Graph()


    for node in graph.nodes:
        G.add_node(node)


    for from_node, edges in graph.edges.items():
        for to_node, weight in edges:
            G.add_edge(from_node, to_node, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=15)
    

    for destination in paths:
        path = []
        node = destination
        while node != initial_node:
            path.append(node)
            node = paths[node]
        path.append(initial_node)
        path.reverse()

        edge_list = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edge_list, width=2, edge_color='r')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.show()


graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph.add_node(node)

graph.add_edge('A', 'B', 7)
graph.add_edge('A', 'C', 9)
graph.add_edge('A', 'F', 14)
graph.add_edge('B', 'C', 10)
graph.add_edge('B', 'D', 15)
graph.add_edge('C', 'D', 11)
graph.add_edge('C', 'F', 2)
graph.add_edge('D', 'E', 6)
graph.add_edge('E', 'F', 9)

initial_node = 'A'
distances, paths = dijkstra(graph, initial_node)

print("Відстані від початкової вершини:")
for node in distances:
    print(f"Від {initial_node} до {node}: {distances[node]}")

print("\nШляхи:")
for destination in paths:
    print(f"Шлях до {destination}: ", end="")
    path = []
    node = destination
    while node != initial_node:
        path.append(node)
        node = paths[node]
    path.append(initial_node)
    path.reverse()
    print(" -> ".join(path))

visualize_graph(graph, paths, initial_node)
