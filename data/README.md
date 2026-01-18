# Data Directory

This directory is for storing network data files. 

## Supported formats:
- CSV files
- JSON files
- GraphML files
- Edge list files
- Adjacency matrices

## Example usage:

```python
import networkx as nx
import pandas as pd

# Load edge list from CSV
edges_df = pd.read_csv('data/raw/network_edges.csv')
G = nx.from_pandas_edgelist(edges_df, 'source', 'target')

# Load from GraphML
G = nx.read_graphml('data/raw/network.graphml')

# Load from edge list
G = nx.read_edgelist('data/raw/network.txt')
```

## Note:
Data files are git-ignored by default to keep the repository clean.
Add `.gitkeep` files to track empty directories.
