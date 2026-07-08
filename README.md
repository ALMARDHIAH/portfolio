# Road Network Analysis in Federal Territory of Putrajaya  (2025)
>**Source of data**: OpenStreetMap  
>**Tools**: Python, OSMnx, NetworkX

## Appreciation
A big thanks to my final year project supervisor, *Prof. Madya Dr. Fatimah Abdul Razak* for guiding me throughout this project and shaping my way of thinking.

## Why analyzing Putrajaya's road network?
In early 2001, the **Federal Administrative Centre of Malaysia** were **relocated** from Kuala Lumpur **to Putrajaya** due to **congestion** issue.
- In the early planning of Putrajaya, an efficient transportation system was emphasized to connect facilities, services, and workplaces.
- The **goal** was to create a **congestion-free** city with public transport-oriented design (Ho Chin Siong, 2006).
- Therefore, understanding the effectiveness and structure of the road network is essential.
- This study conducts a road network analysis to **evaluate** how well **Putrajaya’s network supports its intended goals**.

## Objectives
1. To **construct** the **road network** of Putrajaya, limited to **driveways**, using OpenStreetMap data.
2. To **identify influential nodes** within Putrajaya through road network analysis, focusing on:
- Degree
- Closeness Centrality
- Betweenness Centrality
3. To **identify** the **shortest path** between **influential nodes** within the study area.

## Scope of Study

This study focused on [Putrajaya](http://nominatim.openstreetmap.org/ui/search.html?q=putrajaya) roads limited to **driveways** only.

## Methodology

![Methodology](methodology.png)

## Results
At the end of this project, we discovered
1. Python **Python OSMnx, Python NetworkX** and **OpenStreetMap data** are **essential** for constructing the road network.
2. **Closeness** centrality **concentrated** in the **central area** of Putrajaya.
3. **Betweenness** centrality is **uniformly distributed** throughout Putrajaya.
4. **Strategic routes** lies on **Lebuh Perdana Barat**, **Persiaran Sultan Sallahuddin Abdul Aziz Shah** and **Lebuh Perdana Timur**.

## Conclusion
Overall, these findings suggest that Putrajaya's road network is **well connected** and provides **balanced connectivity**, although **accessibility remains higher in the central area** than at the periphery.
