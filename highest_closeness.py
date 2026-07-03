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

# Mendapatkan bucu dengan nilai kedekatan dji tertinggi
bucu_tertinggi_dji=max(pemusatan_kedekatan_dji,
   key=pemusatan_kedekatan_dji.get)
nilai_tertinggi_dji=max(pemusatan_kedekatan_dji.values())
print("bucu tertinggi", bucu_tertinggi_dji,
 "dengan nilainya", nilai_tertinggi_dji)

# Mendapatkan pemusatan kedekatan (dij)
pemusatan_kedekatan_dij=nx.closeness_centrality(
graf_proj.reverse(),
distance='length')



# Memasukkan nilai kedekatan dij ke dalam GDF bucu
bucu['Pemusatan Kedekatan dij']=bucu.index.map(
pemusatan_kedekatan_dij)

# Memaparkan nilai kedekatan dij tertib menurun
print(bucu[['Pemusatan Kedekatan dij']].sort_values(
by='Pemusatan Kedekatan dij',
ascending=False))

# Mendapatkan bucu dengan nilai kedekatan dij tertinggi
bucu_tertinggi_dij=max(pemusatan_kedekatan_dij,
   key=pemusatan_kedekatan_dij.get)
nilai_tertinggi_dij=max(pemusatan_kedekatan_dij.values())
print("bucu tertinggi", bucu_tertinggi_dij,
 "dengan nilainya", nilai_tertinggi_dij)

# Memplot bucu dengan nilai kedekatan tertinggi
fig, ax = plt.subplots(figsize=(9, 9.5))
tepi.plot(ax=ax,
linewidth=0.3,
edgecolor="dimgray",
zorder=1)

# Tetapkan warna dan saiz bucu
warna_bucu = ['red' if nod == bucu_tertinggi_dji
else 'green' if  nod == nilai_tertinggi_dji
else 'white' for nod in bucu.index]
saiz_bucu = [5 if nod == bucu_tertinggi_dji
else 5 if nod == nilai_tertinggi_dji
else 2.25 for nod in bucu.index]
bucu.plot(ax=ax,
color=warna_bucu,
edgecolor='black',
linewidth=0.1,
markersize=saiz_bucu,
zorder=2,
alpha=0.8)

plt.axis("off")
plt.show()
 
