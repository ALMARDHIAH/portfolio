import osmnx as ox
import matplotlib.pyplot as plt

# Memuat turun data georuang daripada OSM
graf = ox.graph_from_place(
“putrajaya”,
network_type='drive',
simplify=True)

# Mengunjurkan graf berdasarkan UTM
graf_proj=ox.project_graph(graf)

# Memuat turun GeoDataFrame bucu dan tepi rangkaian
bucu, tepi = ox.graph_to_gdfs(graf_proj)

# Memplot rangkaian
fig, ax = ox.plot_graph(
    graf_proj,
    bgcolor='white',
    node_size=1,
    node_color='white',
    node_edgecolor='black',
    node_zorder=3,
    edge_color='black',
    edge_linewidth=1,
    show=False,
    close=False)

figure, ax = plt.subplots(figsize=(8,10))

bucu.plot(ax=ax,
color='white',
markersize=0.65,
alpha=1,
edgecolor='black',
linewidth=0.2,
zorder=2)

tepi.plot(ax=ax,
linewidth=0.25,
edgecolor="black",
zorder=1)
plt.axis('off')
plt.show()
