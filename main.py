import networkx as nx
import matplotlib.pyplot as plt # import Matplotlib plotting inferface

g = nx.Graph()
g.add_edge('a', 'b', weight=0.1)
g.add_edge('b', 'c', weight=1.5)
g.add_edge('a', 'c', weight=1.0)
g.add_edge('c', 'd', weight=2.2)

print(nx.shortest_path(g, 'b', 'd'))
print(nx.shortest_path(g, 'b', 'd', weight='weight'))

# for n in g.nodes():
#     print(n, g[n])

nx.draw(g)
# nx.draw_random(g)
# nx.draw_circular(g)
# nx.draw_spectral(g)
# plt.savefig('graph.png')
