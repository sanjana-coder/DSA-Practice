#graph basic

from collections import defaultdict

n = 8
edges = [[0,1], [1,2], [0,3], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]]

adj_list = defaultdict(list)

for v,e in edges:
	adj_list[v].append(e)

print(adj_list)
print(adj_list[3])

class Node:
	def __init__(self, value):
		self.value = value
		self.nei_nodes = []
		
	def __str__(self):
		print(f'Node({self.value})')
		return
	
	def display(self):
		connections = [curnode.value for curnode in self.nei_nodes]
		print(f'{self.value} is connected to {connections}') 
		return
		
		
A = Node('A')
B = Node('B')
C = Node('C')

A.nei_nodes.append(B)
A.nei_nodes.append(C)

A.display()