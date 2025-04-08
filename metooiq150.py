# [1508]

# 삼각형의 높이
h = int(input())
tri = [[0] * h for _ in range(h)]

# 입력 값들을 첫 번째 열에 할당
for i in range(h):
	num = int(input())
	tri[i][0] = num

# 다음 열
i = 0
for x in range(h - 1):
	for y in range(i, h - 1):
		tri[y + 1][x + 1] = tri[y + 1][x] - tri[y][x]
	i += 1

# 출력
for i in range(h):
	for j in range(h):
		if tri[i][j]:
			print(tri[i][j], end=' ')
	print()