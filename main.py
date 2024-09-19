#!/usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Adding nodes with names
G.add_nodes_from([
    "Switch1",
    "Switch2",
    "Router",
    "Access Point",
    "Server",
    "PC1",
    "PC2",
    "PC3",
    "PC4",
    "PC5",
    "PC6",
    "Laptop1",
    "Laptop2",
    "IP Phone1",
    "IP Phone2",
    "SmartPhone",
    "Server",
    "Scanner",
    "Printer",
    "Internet"
])

G.add_edges_from([
    ("Switch1", "Switch2"),
    ("Switch1", "PC1"),
    ("Switch1", "Router"),
    ("Switch2", "PC2"),
    ("Switch2", "PC3"),
    ("Switch2", "IP Phone1"),
    ("PC2", "Scanner"),
    ("PC2", "Printer"),
    ("PC3", "IP Phone2"),
    ("PC1", "PC4"),
    ("PC1", "PC4"),
    ("PC5", "PC4"),
    ("PC5", "PC6"),
    ("PC1", "PC6"),
    ("Router", "Access Point"),
    ("Router", "Server"),
    ("Router", "Internet"),
    ("Laptop1", "Access Point"),
    ("Laptop2", "Access Point"),
    ("SmartPhone", "Access Point"),
])

# Connect the nodes with each other.
nx.draw(G, with_labels=True, pos={
    "Switch1": (6, 6),
    "Switch2": (8, 6),
    "Router": (6, 4),
    "Access Point": (4, 4),
    "Server": (12, 4),
    "PC1": (6, 8),
    "PC2": (8, 8),
    "PC3": (10, 12),
    "PC4": (4, 8),
    "PC5": (4, 10),
    "PC6": (6, 10),
    "Laptop1": (2, 2),
    "Laptop2": (2, 4),
    "IP Phone1": (12, 6),
    "IP Phone2": (12, 12),
    "SmartPhone": (4, 2),
    "Scanner": (6, 12),
    "Printer": (8, 12),
    "Internet": (2, 6)
})

plt.savefig("ans.png")
