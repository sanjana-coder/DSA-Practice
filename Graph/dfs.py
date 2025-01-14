# dfs

from collections import defaultdict

# DFS Recursive 

def dfs_recursive_internal_stack(source, adj_list, seen):
	print(source, end=" ")
	for nei_node in adj_list[source]:
		if nei_node not in seen:
			seen.add(nei_node)
			dfs_recursive_internal_stack(nei_node, adj_list, seen)
			

def dfs_recursive_external_stack(adj_list, seen, stack):
	if stack:
		cur_node = stack.pop()
		print(cur_node, end = ' ')
		for nei_node in adj_list[cur_node]:
			if nei_node not in seen:
				seen.add(nei_node)
				stack.append(nei_node)
				dfs_recursive_external_stack(adj_list, seen, stack)
		

def dfs_iterative(adj_list, seen, stack):
	while stack:
		cur_node = stack.pop()
		print(cur_node, end=' ')
		for nei_node in adj_list[cur_node]:
			if nei_node not in seen:
				seen.add(nei_node)
				stack.append(nei_node)
			

if __name__ == '__main__':
	n = 8
	edges = [[0,1], [1,2], [0,3], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]]
	
	adj_list = defaultdict(list)
	
	for v,e in edges:
		adj_list[v].append(e)
		
	source = 0
	seen = set()
	seen.add(source)
	stack = [source]
	print("dfs_recursive_internal_stack")
	dfs_recursive_internal_stack(source, adj_list, seen)
	print("\ndfs_recursive_external_stack")
	seen.clear()
	seen.add(source)
	stack = [source]
	dfs_recursive_external_stack(adj_list, seen, stack)
	seen.clear()
	seen.add(source)
	stack = [source]
	print("\ndfs_iterative")
	dfs_iterative(adj_list, seen, stack)