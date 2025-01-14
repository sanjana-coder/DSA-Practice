#BFS

from collections import defaultdict

def bfs(adj_list, seen, queue):
	while queue:
		cur_node = queue.pop(0)
		print(cur_node, end=' ')
		for nei_node in adj_list[cur_node]:
			if nei_node not in seen:
				seen.add(nei_node)
				queue.append(nei_node)


if __name__ == '__main__':
	n = 8
	edges = [[0,1], [1,2], [0,3], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]]
	
	adj_list = defaultdict(list)
	
	for v,e in edges:
		adj_list[v].append(e)
		
	source = 0
	seen = set()
	seen.add(source)
	queue = [source]
	
	bfs(adj_list, seen, queue)
	
	