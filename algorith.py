import maze

graph = [list(x) for x in maze.the_maze]

def floydWarShall(graph):

	num_of_nodes = len(graph)

	# initial distances set to infinity
	distance = [[5] * num_of_nodes for _ in range(num_of_nodes)]

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


def reconstruct_path(start_node, end_node, distance):
	# this is not my code, they made me do it.....

	path = [end_node]

	while end_node != start_node:
		for k in range(len(graph)):
			if distance[start_node][k] + distance[k][end_node] == distance[start_node][end_node]:
				path.append(k)
				end_node = k
				 
		return path


distance = floydWarShall(graph)
# a = reconstruct_path(6, 2, distance)
# print(a)