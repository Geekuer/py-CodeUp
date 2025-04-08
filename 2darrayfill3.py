# [1505]

num = int(input())
matrix = [[0] * (num + 2) for _ in range(num + 2)]
x, y = 0, 1

for i in range(1, num ** 2 + 1):
	if x < num and not matrix[y][x + 1]: # 우
		if y > 1 and not matrix[y - 1][x]: # 상
			matrix[y - 1][x] = i
			y -= 1

		else:
			matrix[y][x + 1] = i # 우
			x += 1

	elif y < num and not matrix[y + 1][x]: # 하
		matrix[y + 1][x] = i
		y += 1

	elif x > 1 and not matrix[y][x - 1]: # 좌
		matrix[y][x - 1] = i
		x -= 1

	elif y > 1 and not matrix[y - 1][x]: # 상
		matrix[y - 1][x] = i
		y -= 1
		

for i in range(1, num + 1):
	for j in range(1, num + 1):
		print(matrix[i][j], end=' ')
	
	print()