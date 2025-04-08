# [1515]

matrix = [list(input().split()) for _ in range(25)]
matrix_cp = [row[:] for row in matrix]
count = 0

for y in range(25):
	for x in range(25):
		count = 0
		
		for yc in range(-1, 2):
			for xc in range(-1, 2):
				if not (yc == 0 and xc == 0):
					if (0 <= y + yc < 25 and 0 <= x + xc < 25) and matrix[y + yc][x + xc] == '1':
						count += 1

		if matrix[y][x] == '0': # 생명이 없는 칸
			if count == 3:
				matrix_cp[y][x] = '1' # 생명 탄생
			
		else: # 생명이 있는 칸
			if count >= 4 or count <= 1:
				matrix_cp[y][x] = '0' # 생명 사망
					
for row in matrix_cp:
	for item in row:
		print(item, end=' ')
	print()