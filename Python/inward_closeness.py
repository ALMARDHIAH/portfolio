import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Memuat turun data georuang daripada OSM
graf = ox.graph_from_place(
“putrajaya”,
network_type='drive',
simplify=True)

# Mengunjurkan graf berdasarkan UTM
graf_proj=ox.project_graph(graf)

# Memuat turun GeoDataFrame bucu dan tepi rangkaian
bucu, tepi= ox.graph_to_gdfs(graf_proj)

# Mendapatkan pemusatan kedekatan (dji)
pemusatan_kedekatan_dji=nx.closeness_centrality(
graf_proj,
distance='length')

# Memasukkan nilai kedekatan dji ke dalam GDF bucu
bucu['Pemusatan Kedekatan dji']=bucu.index.map(
pemusatan_kedekatan_dji)

# Memaparkan nilai kedekatan dji tertib menurun
print(bucu[['Pemusatan Kedekatan dji']].sort_values(
by='Pemusatan Kedekatan dji',
ascending=False))

# Memplot kedekatan dji bagi setiap bucu
figure, ax = plt.subplots(figsize=(10,10.5))
tepi.plot(ax=ax,
linewidth=0.3,
edgecolor="dimgray",
zorder=1)
bucu.plot(ax=ax, markersize=1,
column='Pemusatan Kedekatan dji',
cmap="rainbow", legend=True, 
alpha=0.95, zorder=2)

plt.axis('off')
plt.show()
