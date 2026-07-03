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

# Mendapatkan bucu dengan nilai pengantaraan tertinggi
bucu_tertinggi=max(pemusatan_pengantaraan,
    key=pemusatan_pengantaraan.get)
nilai_tertinggi=max(pemusatan_pengantaraan.values())
print("bucu tertinggi", bucu_tertinggi,
 "dengan nilainya", nilai_tertinggi)

# Memplot bucu dengan nilai pengantaraan tertinggi
fig, ax = plt.subplots(figsize=(8, 8.5))

tepi.plot(ax=ax,
linewidth=0.3,
edgecolor="dimgray",
zorder=1)

# Tetapkan warna dan saiz bucu
warna_bucu = ['red' if nod == bucu_tertinggi
else 'white' for nod in bucu.index]
saiz_bucu = [5 if nod == bucu_tertinggi
else 0 for nod in bucu.index]
bucu.plot(ax=ax,
color=warna_bucu,
markersize=saiz_bucu,
zorder=2,
alpha=0.8)

plt.axis("off")
plt.show()
