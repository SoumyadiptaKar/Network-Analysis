"""
Graph Analysis Examples

This module demonstrates various graph analysis techniques including
centrality measures, clustering, and path analysis.
"""

import networkx as nx
import matplotlib.pyplot as plt


def create_sample_network():
    """Create a sample social network for analysis."""
    G = nx.Graph()
    
    edges = [
        ('Alice', 'Bob'), ('Alice', 'Charlie'), ('Alice', 'David'),
        ('Bob', 'Charlie'), ('Bob', 'Eve'),
        ('Charlie', 'David'), ('Charlie', 'Frank'),
        ('David', 'Frank'),
        ('Eve', 'Grace'), ('Eve', 'Henry'),
        ('Frank', 'Grace'),
        ('Grace', 'Henry')
    ]
    
    G.add_edges_from(edges)
    return G


def analyze_centrality(G):
    """Compute and display various centrality measures."""
    print("\n=== Centrality Analysis ===")
    
    # Degree centrality
    degree_cent = nx.degree_centrality(G)
    print("\nDegree Centrality (top 3):")
    top_degree = sorted(degree_cent.items(), key=lambda x: x[1], reverse=True)[:3]
    for node, cent in top_degree:
        print(f"  {node}: {cent:.3f}")
    
    # Betweenness centrality
    between_cent = nx.betweenness_centrality(G)
    print("\nBetweenness Centrality (top 3):")
    top_between = sorted(between_cent.items(), key=lambda x: x[1], reverse=True)[:3]
    for node, cent in top_between:
        print(f"  {node}: {cent:.3f}")
    
    # Closeness centrality
    close_cent = nx.closeness_centrality(G)
    print("\nCloseness Centrality (top 3):")
    top_close = sorted(close_cent.items(), key=lambda x: x[1], reverse=True)[:3]
    for node, cent in top_close:
        print(f"  {node}: {cent:.3f}")
    
    return between_cent


def analyze_clustering(G):
    """Analyze clustering in the graph."""
    print("\n=== Clustering Analysis ===")
    
    # Clustering coefficient
    clustering = nx.clustering(G)
    avg_clustering = nx.average_clustering(G)
    
    print(f"Average clustering coefficient: {avg_clustering:.3f}")
    print("\nTop 3 nodes by clustering coefficient:")
    top_clustering = sorted(clustering.items(), key=lambda x: x[1], reverse=True)[:3]
    for node, coef in top_clustering:
        print(f"  {node}: {coef:.3f}")


def analyze_paths(G):
    """Analyze paths in the graph."""
    print("\n=== Path Analysis ===")
    
    # Average shortest path length
    if nx.is_connected(G):
        avg_path = nx.average_shortest_path_length(G)
        diameter = nx.diameter(G)
        print(f"Average shortest path length: {avg_path:.3f}")
        print(f"Diameter: {diameter}")
    else:
        print("Graph is not connected")
    
    # Example shortest path
    nodes = list(G.nodes())
    if len(nodes) >= 2:
        source, target = nodes[0], nodes[-1]
        path = nx.shortest_path(G, source, target)
        print(f"\nShortest path from {source} to {target}:")
        print(f"  {' -> '.join(path)}")


def visualize_network(G, centrality_measure=None, title="Network"):
    """Visualize the network with optional centrality coloring."""
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    
    if centrality_measure:
        # Size and color by centrality
        node_sizes = [5000 * centrality_measure[node] + 500 for node in G.nodes()]
        node_colors = [centrality_measure[node] for node in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_size=node_sizes,
                node_color=node_colors, cmap='YlOrRd',
                font_size=10, font_weight='bold',
                edge_color='gray', width=2)
    else:
        nx.draw(G, pos, with_labels=True, node_color='lightblue',
                node_size=1000, font_size=10, font_weight='bold',
                edge_color='gray', width=2)
    
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def main():
    """Main function to demonstrate graph analysis."""
    # Create sample network
    G = create_sample_network()
    
    print("=== Network Properties ===")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Density: {nx.density(G):.3f}")
    print(f"Is connected: {nx.is_connected(G)}")
    
    # Perform analyses
    between_cent = analyze_centrality(G)
    analyze_clustering(G)
    analyze_paths(G)
    
    # Visualize
    print("\nGenerating visualizations...")
    visualize_network(G, title="Social Network")
    visualize_network(G, between_cent, "Network (sized by Betweenness Centrality)")


if __name__ == "__main__":
    main()
