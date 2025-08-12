def printHTMLOutput(matrix):
	html_lines = [
		"<!doctype html>",
		"<html>",
		"<head><meta charset='utf-8'><title>Matrice</title></head>",
		"<body>",
		"<table border=1 cellpadding='4' cellspacing='0'>"
	]

	for i in range(len(matrix)):
		html_lines.append("<tr>")
		for j in range(len(matrix[i])):
			if matrix[i][j] == 0:
				html_lines.append(f"<td style='background-color:white;'></td>")
			else:
				html_lines.append(f"<td style='background-color:black;'></td>")
		html_lines.append("</tr>")

	html_lines.extend([
        "</table>",
        "</body>",
        "</html>"
    ])
	html_output = "\n".join(html_lines)
	try:
		with open("index.html", "w", encoding="utf-8") as f:
			f.write(html_output)
		f.close
	except OSError as e:
		print(f"Error while open or write index.html: {e}")
		return
	print("--> \033[32mindex.html generate with success\033[0m")
	


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
		[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
		[1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		]
	n_turn = 5
	result = gameOfLife(matrix, n_turn)
	print(result)
	printHTMLOutput(result)