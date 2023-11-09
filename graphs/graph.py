import networkx as nx
import matplotlib.pyplot as plt

# Initialize an empty graph represented as an adjacency list
graph = {}

# List of pairs representing edges
edges = [
    ("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D"), ("D", "E"),
    ("D", "F"), ("E", "F"), ("G", "H"), ("H", "I"), ("I", "G"),
    ("J", "K"), ("K", "L"), ("L", "J"), ("J", "M"), ("K", "N"), ("L", "O"),
    ("M", "N"), ("N", "O")
]

edges_properties = {
    "GH":[("Tuesday", "Port 69"), ("Tuesday", "Port 69"), ("Tuesday", "Port 440"), ("Wednesday", "Port 4")],
    "HG":[("Tuesday", "Port 69"), ("Tuesday", "Port 69"), ("Wednesday", "Port 4")]
}

# Descriptions for some nodes
node_descriptions = {
    "M": "M Node",
    "G": "G Node",
}

# Reconstruct the graph
for u, v in edges:
    # Add nodes u and v if not already present
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    # Add the edge between u and v
    graph[u].append(v)
    graph[v].append(u)  # If the graph is undirected, add this line

# Create a NetworkX graph from the adjacency list
G = nx.Graph(graph)

# Define node colors
node_colors = ['red' if node.startswith('M') or node.startswith('G') else 'skyblue' for node in G.nodes()]

# Draw the graph with labels and descriptions
pos = nx.spring_layout(G)
labels = {node: node_descriptions.get(node, "") for node in G.nodes()}
nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=12)
nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_color='black', verticalalignment='bottom')
plt.title("Reconstructed Graph with Descriptions")

print(G.nodes())

print(G.number_of_nodes())

print(sorted(nx.neighbors(G, "M")))

print(nx.density(G))

print(sorted(nx.all_neighbors(G, "M")))

print(sorted(nx.common_neighbors(G, "M", "L")))

plt.show()

