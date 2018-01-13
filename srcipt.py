import networkx as nx 
import copy
import pandas as pd 
import matplotlib.pyplot as plt 
import itertools

edgelist = pd.read_csv('https://gist.githubusercontent.com/brooksandrew/e570c38bcc72a8d102422f2af836513b/raw/89c76b2563dbc0e88384719a35cba0dfc04cd522/edgelist_sleeping_giant.csv')
nodelist = pd.read_csv('https://gist.githubusercontent.com/brooksandrew/f989e10af17fb4c85b11409fea47895b/raw/a3a8da0fa5b094f1ca9d82e1642b384889ae16e8/nodelist_sleeping_giant.csv')
df = pd.DataFrame(nodelist)
de = pd.DataFrame(edgelist)
g = nx.Graph()
print(edgelist.head(10))

for index, row in df.iterrows():
	g.add_node(row['id'] , pos = (row['X'], row['Y']))
'''
for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())
'''
for index, row in de.iterrows():
	g.add_edge(row['node1'], row['node2'], weight = row['distance'], id=index, color = row['color'])


print('# of edges: {}'.format(g.number_of_edges()))
print('# of nodes: {}'.format(g.number_of_nodes()))

node_positions = {node[0] : node[1] for node in g.nodes(data = True)} 

edge_colors = [e[2]['color'] for e in g.edges(data = True)]

plt.figure(figsize=(8,6))
#pos = nx.spring_layout(g)
#nx.draw_networkx_nodes(g, pos, cmap = plt.get_cmap('jet'), node_color = 'black',node_size = 10,  arrows=True)
#nx.draw_networkx_labels(g, pos)
#nx.draw_networkx_edges(g,)
nx.draw(g,pos=nx.spring_layout(g), edge_color=edge_colors, node_size=10, node_color='black')
plt.show()