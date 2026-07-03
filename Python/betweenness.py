import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Memuat turun data georuang daripada OSM
graf = ox.graph_from_place(“putrajaya”,
   network_type='drive',
   simplify=True)

# Mengunjurkan graf berdasarkan UTM
graf_proj=ox.project_graph(graf)

# Memuat turun GeoDataFrame bucu dan tepi rangkaian
bucu, tepi= ox.graph_to_gdfs(graf_proj)

# Mendapatkan pemusatan pengantaraan
pemusatan_pengantaraan=nx.betweenness_centrality(
   graf_proj,
   weight='length',
   normalized=True)

# Memasukkan nilai pengantaraan ke dalam GDF bucu
bucu['Pemusatan Pengantaraan']=bucu.index.map(
 pemusatan_pengantaraan)

# Memaparkan nilai pengantaraan mengikut tertib menurun
print(bucu[['Pemusatan Pengantaraan']].sort_values(
by='Pemusatan Pengantaraan',
ascending=False))

# Memplot nilai pengantaraan bagi setiap bucu
figure, ax = plt.subplots(figsize=(9,9.5))
bucu.plot(ax=ax,
markersize=1,
column='Pemusatan Pengantaraan',
cmap="rainbow",
legend=True,
alpha=0.95,
zorder=2)
tepi.plot(ax=ax,
linewidth=0.3,
edgecolor="dimgray",
zorder=1)

plt.axis('off')
plt.show()
