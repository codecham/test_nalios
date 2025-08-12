def numberOfAliveNeighbors(matrix, i, j):
	count = 0

	for pos_i in range(i - 1, i + 2):
		for pos_j in range(j - 1, j + 2):
			if (pos_i == i and pos_j == j):
				continue
			
			if 0 <= pos_i < len(matrix) and 0 <= pos_j < len(matrix):
				if matrix[pos_i][pos_j] == 1:
					count += 1
	return count


def checkCell(matrix, i, j):
	nb_neighbors = numberOfAliveNeighbors(matrix, i, j)
	if matrix[i][j] == 0:
		if nb_neighbors == 3:
			return 1
		else:
			return 0
	else:
		if nb_neighbors == 2 or nb_neighbors == 3:
			return 1
		else:
			return 0

def makeTurn(matrix):
	new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			new_matrix[i][j] = checkCell(matrix, i, j)
	return new_matrix

def gameOfLife(matrix, n_turn):
	for turn in range(n_turn):
		matrix = makeTurn(matrix)
	return matrix

if __name__ == "__main__":
	matrix = [
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		]
	n_turn = 5
	print(gameOfLife(matrix, n_turn))