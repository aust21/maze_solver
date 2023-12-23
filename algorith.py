import maze

def floydWarShall(graph):

	num_of_nodes = len(graph)

	# initial distances set to infinity
	distance = [[float("inf")] * num_of_nodes for _ in range(num_of_nodes)]

	# set the distance from a node to itself to zero
	for i in range(num_of_nodes):
		distance[i][i] = 0

	# if there is no obstacle "x"; set distance to 1
	for i in range(num_of_nodes):
		for j in range(num_of_nodes):
			if graph[i][j] != "x":
				distance[i][j] = 1


	for k in range(num_of_nodes):
		for i in range(num_of_nodes):
			for j in range(num_of_nodes):
				distance[i][j] = min(distance[i][j], distance[k][i] + distance[k][j])

	return distance

graph = maze.the_maze