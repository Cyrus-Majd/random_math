import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (4, 6), (70, 22), (22, 54)])

# List of nodes for the subgraph
subgraph_nodes = [1, 2, 3, 22]

# Extract the subgraph
subgraph = G.subgraph(subgraph_nodes)

# Visualize the original graph and the subgraph
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 4))

# Plot the original graph
plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=12)
plt.title("Original Graph")

# Plot the subgraph
plt.subplot(122)
nx.draw(subgraph, with_labels=True, node_size=500, node_color='lightcoral', font_size=12)
plt.title("Subgraph")

plt.tight_layout()
plt.show()
