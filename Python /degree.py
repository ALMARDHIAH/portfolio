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

# Mendapatkan darjah
darjah=nx.degree(graf_proj)

# Memasukkan lajur ‘darjah’ ke dalam GeoDataFrame bucu
bucu['darjah']=bucu.index.map(darjah)

# Memaparkan ‘darjah’ mengikut tertib menurun
print(bucu[['darjah']].sort_values(by='darjah',ascending=False))

# Memplot darjah bagi setiap bucu dalam rangkaian
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
