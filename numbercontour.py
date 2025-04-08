# [1512]

size = int(input())
y, x = map(int, input().split())
y -= 1
x -= 1

_list = [[None] * size for _ in range(size)]

for _y in range(size):
	for _x in range(size):
		dist = abs(x - _x) + abs(y - _y)
		_list[_y][_x] = dist + 1

for row in _list:
	for item in row:
		print(item, end=' ')
	print()