import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Downloading geospatial data from OSM
graf = ox.graph_from_place(
“putrajaya”,
network_type='drive',
simplify=True)

# Projecting the graph based on UTM
graf_proj=ox.project_graph(graf)

# Downloading GeoDataFrame of nodes and edges
bucu, tepi= ox.graph_to_gdfs(graf_proj)

# Identifying the degree of each node
darjah=nx.degree(graf_proj)

# Inserting ‘degree’ row into the node GeoDataFrame
bucu['darjah']=bucu.index.map(darjah)

# Showing ‘darjah’ in descending order
print(bucu[['darjah']].sort_values(by='darjah',ascending=False))

# Plotting the degree of each node in the network
figure, ax = plt.subplots(figsize=(8.5,8))
bucu.plot(ax=ax, markersize=1, 
          column='darjah', 
          cmap= 'rainbow', legend=True, 
          alpha=0.95, zorder=2
          #, edgecolor='black',linewidth=0.05
          )
tepi.plot(ax=ax, linewidth=0.3, edgecolor="dimgray", zorder=1)

plt.axis('off')
plt.show()
