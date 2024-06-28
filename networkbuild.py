import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd



G= nx.MultiGraph()
df = pd.read_csv("ecommerce_data.csv",nrows=10)

for index, row in df.iterrows():
    G.add_node(row['entity_type'], type='entity', label=row['entity_type'])
    G.add_node(row['second_entity'], type='entity', label=row['second_entity'])
    G.add_edge(row['entity_type'], row['second_entity'], relationship=row['relationship'])

pos = nx.spring_layout(G)

# Draw nodes and labels
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'))


# Draw edges with weights
edge_labels = nx.get_edge_attributes(G, 'relationship')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_edges(G, pos)

# # Show graph
# plt.axis('off')
# plt.show()


# nx.draw(G, with_labels=True, with_edges=True)
# # plt.show()


# nx.draw_spring(G, with_labels = True)
plt.savefig("filename5.png")

#   
# # Write to GEXF file 
nx.write_gexf(G, "ecommerce_data.gexf")



