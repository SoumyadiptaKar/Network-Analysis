"""
Basic Graph Creation Examples

This module demonstrates how to create and manipulate different types of graphs
using NetworkX.
"""

import networkx as nx
import matplotlib.pyplot as plt


def create_undirected_graph():
    """Create a simple undirected graph."""
    G = nx.Graph()
    
    # Add nodes
    G.add_nodes_from([1, 2, 3, 4, 5])
    
    # Add edges
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
    
    return G


def create_directed_graph():
    """Create a directed graph."""
    DG = nx.DiGraph()
    
    # Add edges (nodes are created automatically)
    DG.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'D'),
        ('D', 'E')
    ])
    
    return DG


def create_weighted_graph():
    """Create a weighted graph."""
    WG = nx.Graph()
    
    # Add weighted edges
    WG.add_edge('X', 'Y', weight=0.5)
    WG.add_edge('X', 'Z', weight=1.5)
    WG.add_edge('Y', 'Z', weight=2.0)
    WG.add_edge('Y', 'W', weight=1.0)
    
    return WG


def visualize_graph(G, title="Graph", node_color='lightblue'):
    """Visualize a graph."""
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    
    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color=node_color,
            node_size=500, font_size=12, font_weight='bold',
            edge_color='gray', width=2)
    
    # If the graph has weights, draw them
    if nx.is_weighted(G):
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def main():
    """Main function to demonstrate graph creation."""
    # Create and visualize undirected graph
    print("Creating undirected graph...")
    G = create_undirected_graph()
    print(f"Nodes: {G.nodes()}")
    print(f"Edges: {G.edges()}")
    visualize_graph(G, "Undirected Graph", 'lightblue')
    
    # Create and visualize directed graph
    print("\nCreating directed graph...")
    DG = create_directed_graph()
    print(f"Nodes: {DG.nodes()}")
    print(f"Edges: {DG.edges()}")
    visualize_graph(DG, "Directed Graph", 'lightcoral')
    
    # Create and visualize weighted graph
    print("\nCreating weighted graph...")
    WG = create_weighted_graph()
    print(f"Nodes: {WG.nodes()}")
    print(f"Edges with weights:")
    for u, v, d in WG.edges(data=True):
        print(f"  {u}-{v}: {d['weight']}")
    visualize_graph(WG, "Weighted Graph", 'lightgreen')


if __name__ == "__main__":
    main()
