#graph basic

from collections import defaultdict

n = 8
edges = [[0,1], [1,2], [0,3], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]]

adj_list = defaultdict(list)

for v,e in edges:
	adj_list[v].append(e)

print(adj_list)
print(adj_list[3])