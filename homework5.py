import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from nxviz import CircosPlot

# read data
# split the data in personal into two file to create an index file named emails
# previously change 'date' to DATE type in excel
personal = pd.read_csv("F:/UIUC/590DV/homework5/personalemail.csv")
emails = pd.read_csv("F:/UIUC/590DV/homework5/personal_sender_receiver.csv")

# initialize graph
G = nx.DiGraph()


# add in the node attribute
for d in emails.to_dict("records"):
    node_id = d.pop("id")
    G.add_node(node_id, **d)

# add edges
counts = personal.groupby(["sender_id", "receiver_id"])["id"].count().reset_index()
for d in counts.to_dict("records"):
    G.add_edge(d["sender_id"], d["receiver_id"], count=d["id"])


# filtered graph
nx.draw(G, pos=nx.random_layout(G),with_labels = True,node_size =20,node_color = 'y',edge_color = 'r')
plt.savefig("F:/UIUC/590DV/homework5/personal_email1.png", dpi=300)
nx.draw(G,pos = nx.spring_layout(G),with_labels = True,node_size =20,node_color = 'k',edge_color = 'r')
plt.savefig("F:/UIUC/590DV/homework5/personal_email2.png", dpi=300)
nx.draw(G,pos = nx.circular_layout(G),with_labels = True,node_size =20,node_color = 'w',edge_color = 'r')
plt.savefig("F:/UIUC/590DV/homework5/personal_email3.png", dpi=300)
nx.draw(G,pos = nx.shell_layout(G),with_labels = True,node_size =20,node_color = 'b',edge_color = 'r')
plt.savefig("F:/UIUC/590DV/homework5/personal_email4.png", dpi=300)

# Use a Circos Plot
c = CircosPlot(G, radius=10, nodecolor = "blue", edgecolor = "red")
c.draw()
plt.savefig("F:/UIUC/590DV/homework5/personal_email.png", dpi=300)
