import algorith

def show_solution(distance):
	for dist in distance:
		print(dist)


distance = algorith.floydWarShall(algorith.graph)


if __name__ == "__main__":
	show_solution(distance)