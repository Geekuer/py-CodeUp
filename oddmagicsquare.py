# [1510]

# 1. 시작은 첫 행, 한 가운데 열에 1을 둔다.

# 2. 행을 감소, 열을 증가하면서 순차적으로 수를 넣어간다.

# 3. 행은 감소하므로 첫 행보다 작아지는 경우에는 마지막 행으로 넘어간다.

# 4. 열은 증가하므로 마지막 열보다 커지는 경우에는 첫 열로 넘어간다.

# 5. 넣은 수가 n의 배수이면 행만 증가한다. 열은 변화없음.

# 8 1 6 
# 3 5 7 
# 4 9 2 

num = int(input())
num_list = [[None] * num for _ in range(num)]

x = num // 2
y = 0

for i in range(1, num * num + 1):
	num_list[y][x] = i

	if i % num == 0:
		y += 1

	else:
		y -= 1 # 행 감소
		x += 1 # 열 증가
	
	if y <= -1: # 마지막 행
		y = num - 1

	if x >= num: # 첫 열
		x = 0

for i in num_list:
	for j in i:
		print(j, end=' ')
	
	print()