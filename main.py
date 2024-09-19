#!/usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image

G = nx.Graph()

icons = {
    "router": "icon/router.png",
    "switch": "icon/switch.png",
    "pc": "icon/pc.jpg",
    "accesspoint": "icon/accessPoint.png",
    "server": "icon/server.png",
    "Laptop": "icon/laptop.jpg",
    "phone": "icon/phone.png",
    "internet": "icon/internet.png",
    "scanner": "icon/scanner.jpg",
    "printer": "icon/printer.jpg",
    "ipphone": "icon/phone.png",
}

images = {k: Image.open(fname) for k, fname in icons.items()}

# Adding nodes with names
G.add_node("Switch1", image=images["switch"])
G.add_node("Switch2", image=images["switch"])
G.add_node("Router", image=images["router"])
G.add_node("Access Point", image=images["accesspoint"])
G.add_node("Server", image=images["server"])
for i in range(6):
    G.add_node("PC" + str(i + 1), image=images["pc"])
G.add_node("Laptop1", image=images["Laptop"])
G.add_node("Laptop2", image=images["Laptop"])
G.add_node("IP Phone1", image=images["ipphone"])
G.add_node("IP Phone2", image=images["ipphone"])
G.add_node("SmartPhone", image=images["phone"])
G.add_node("Server", image=images["server"])
G.add_node("Scanner", image=images["scanner"])
G.add_node("Printer", image=images["printer"])
G.add_node("Internet", image=images["internet"])

edges = [
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
]

G.add_edges_from(edges)

pos = {
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
}

fig, ax = plt.subplots()

nx.draw(G, pos=pos)

tr_figure = ax.transData.transform
tr_axes = fig.transFigure.inverted().transform

icon_size = (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.006
icon_center = icon_size / 2.0

for n in G.nodes:
    xf, yf = tr_figure(pos[n])
    xa, ya = tr_axes((xf, yf))
    a = plt.axes([xa - icon_center, ya - icon_center, icon_size, icon_size])
    a.imshow(G.nodes[n]["image"])
    a.axis("off")

plt.show()
plt.savefig("ans.png")
