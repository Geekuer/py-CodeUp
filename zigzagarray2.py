# [1504]

num = int(input())
matrix = [[None for _ in range(num)] for _ in range(num)]

for col in range(num):
	for row in range(num):
		if col % 2 == 0:
			matrix[col][row] = num * col + (row + 1)

		else:
			matrix[col][row] = num * (col + 1) - row

for col in range(num):
	for row in matrix:
		print(row[col], end=' ')
	
	print()