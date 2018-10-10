graph13 = [
	{2:3, 3:4, 4:7, 5:9}, # 1
	{6:3}, # 2
	{7:7}, # 3
	{6:6, 8:6}, # 4
	{8:9, 7:4}, # 5
	{10:8}, # 6
	{9:5}, # 7
	{9:4}, # 8
	{11:7}, # 9
	{11:4}, # 10
	{} # 11
]

graph14 = [
	{2:7, 3:1}, # 1
	{4:2, 5:9}, # 2
	{5:5, 6:4}, # 3
	{7:4, 8:7}, # 4
	{8:3, 10:5, 9:6}, # 5
	{9:2}, # 6
	{11:3}, # 7
	{11:2}, # 8
	{11:8}, # 9
	{11:7}, # 10
	{} # 11
]

if __name__ == "__main__":
	graph = graph14
	result = [0 for i in graph]
	nodes = [[] for i in graph]
	for i in range(len(graph)-1, -1, -1):
		paths = []
		for node in graph[i]:
			path = result[node-1] + graph[i][node]
			paths.append((path, node))
		if paths:
			minpath = min(paths)
			result[i] = minpath[0]
			nodes[i] = [minpath[1]] + nodes[minpath[1] - 1]

	print(result[0])
	print(nodes[0])
