# [※1520]

# 입력
xs, ys = map(int, input().split())

bornnum, alivenum, dienum = map(int, input().split())

matrix = []
for _ in range(ys):
	matrix.append(input().split())

renum = int(input())


for _ in range(renum):
	# 리스트 복사
	matrix_cp = [row[:] for row in matrix]

	# 리스트 반복
	for y in range(ys):
		for x in range(xs):
			lifecount = 0 # 주변 생명 수 초기화
			
			# 주변 8칸 반복
			for yc in range(-1, 2):
				for xc in range(-1, 2):
					if not (yc == 0 and xc == 0): # 현재 칸이 아닐 때만
						if (0 <= y + yc < ys and 0 <= x + xc < xs) and matrix[y + yc][x + xc] == '1': # 인덱스 내 범위인지 확인 and 생명이 있는 칸인지 확인
							lifecount += 1

			if matrix[y][x] == '0': # 생명이 없는 칸
				if lifecount == bornnum: # 생명이 태어나기 위한 이웃 수
					matrix_cp[y][x] = '1' # 생명 탄생
				
			else: # 생명이 있는 칸
				if lifecount < alivenum or lifecount >= dienum: # 생명이 살기 위해 필요한 최소 이웃 수, 생명이 죽는 최소 이웃 수
					matrix_cp[y][x] = '0' # 생명 사망

	# 참조 리스트 변경
	matrix = [row[:] for row in matrix_cp]

# 출력				
for row in matrix:
	for item in row:
		print(item, end=' ')
	print()