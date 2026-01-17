"""
Random Graph Models

This module demonstrates different random graph generation models
and their properties.
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def erdos_renyi_model(n=30, p=0.1):
    """
    Generate an Erdős-Rényi random graph.
    
    Parameters:
    -----------
    n : int
        Number of nodes
    p : float
        Probability of edge creation
    
    Returns:
    --------
    G : NetworkX Graph
    """
    return nx.erdos_renyi_graph(n, p, seed=42)


def barabasi_albert_model(n=30, m=2):
    """
    Generate a Barabási-Albert scale-free network.
    
    Parameters:
    -----------
    n : int
        Number of nodes
    m : int
        Number of edges to attach from a new node
    
    Returns:
    --------
    G : NetworkX Graph
    """
    return nx.barabasi_albert_graph(n, m, seed=42)


def watts_strogatz_model(n=30, k=4, p=0.3):
    """
    Generate a Watts-Strogatz small-world network.
    
    Parameters:
    -----------
    n : int
        Number of nodes
    k : int
        Each node is connected to k nearest neighbors
    p : float
        Probability of rewiring each edge
    
    Returns:
    --------
    G : NetworkX Graph
    """
    return nx.watts_strogatz_graph(n, k, p, seed=42)


def compare_models():
    """Compare properties of different random graph models."""
    # Generate graphs
    er = erdos_renyi_model()
    ba = barabasi_albert_model()
    ws = watts_strogatz_model()
    
    models = [er, ba, ws]
    names = ['Erdős-Rényi', 'Barabási-Albert', 'Watts-Strogatz']
    
    print("=== Comparison of Random Graph Models ===\n")
    
    for model, name in zip(models, names):
        print(f"{name}:")
        print(f"  Nodes: {model.number_of_nodes()}")
        print(f"  Edges: {model.number_of_edges()}")
        print(f"  Density: {nx.density(model):.4f}")
        print(f"  Average clustering: {nx.average_clustering(model):.4f}")
        
        if nx.is_connected(model):
            print(f"  Average path length: {nx.average_shortest_path_length(model):.4f}")
        else:
            print(f"  Graph is not connected")
        
        print()


def visualize_models():
    """Visualize different random graph models."""
    # Generate graphs
    er = erdos_renyi_model(n=20, p=0.15)
    ba = barabasi_albert_model(n=20, m=2)
    ws = watts_strogatz_model(n=20, k=4, p=0.3)
    
    models = [er, ba, ws]
    names = ['Erdős-Rényi\n(Random)', 'Barabási-Albert\n(Scale-free)', 
             'Watts-Strogatz\n(Small-world)']
    colors = ['lightblue', 'lightcoral', 'lightgreen']
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for ax, model, name, color in zip(axes, models, names, colors):
        pos = nx.spring_layout(model, seed=42)
        nx.draw(model, pos, ax=ax, node_color=color, node_size=300,
                with_labels=False, edge_color='gray', width=1)
        ax.set_title(name, fontsize=14, fontweight='bold')
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()


def degree_distribution_comparison():
    """Compare degree distributions of different models."""
    # Generate larger graphs for better statistics
    er = erdos_renyi_model(n=100, p=0.08)
    ba = barabasi_albert_model(n=100, m=4)
    
    # Get degree sequences
    er_degrees = sorted([d for n, d in er.degree()], reverse=True)
    ba_degrees = sorted([d for n, d in ba.degree()], reverse=True)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Erdős-Rényi
    ax1.hist(er_degrees, bins=20, color='lightblue', edgecolor='black')
    ax1.set_xlabel('Degree', fontsize=12)
    ax1.set_ylabel('Frequency', fontsize=12)
    ax1.set_title('Erdős-Rényi Degree Distribution', fontsize=14, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    
    # Barabási-Albert (log-log scale to show power law)
    degree_count = {}
    for degree in ba_degrees:
        degree_count[degree] = degree_count.get(degree, 0) + 1
    
    degrees = list(degree_count.keys())
    counts = list(degree_count.values())
    
    ax2.loglog(degrees, counts, 'o', color='coral')
    ax2.set_xlabel('Degree (log scale)', fontsize=12)
    ax2.set_ylabel('Frequency (log scale)', fontsize=12)
    ax2.set_title('Barabási-Albert Degree Distribution\\n(Power Law)', 
                  fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def main():
    """Main function to demonstrate random graph models."""
    print("Generating and comparing random graph models...\n")
    
    # Compare properties
    compare_models()
    
    # Visualize models
    print("Generating visualizations...")
    visualize_models()
    
    # Compare degree distributions
    print("Comparing degree distributions...")
    degree_distribution_comparison()


if __name__ == "__main__":
    main()
