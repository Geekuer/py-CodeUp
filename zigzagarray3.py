# [1513]

input_num = int(input())
_list = [['0'] * input_num for _ in range(input_num)]

x = 0
y = input_num - 1
_dir = 'NE'

for i in range(1, input_num ** 2):
	if x == input_num - 1 and y == input_num - 1:
		_list[y][x] = str(i)
		break
	
	if (x == input_num - 1) and (_list[y + 1][x - 1] != '0'): # ↓
		_list[y][x] = str(i)
		y += 1
		_dir = 'SW'
		
	elif _dir == 'SW':
		if y == input_num - 1:  # →
			_list[y][x] = str(i)
			x += 1
			_dir = 'NE'
		
		elif (_list[y + 1][x - 1] == '0'): # ↙
			_list[y][x] = str(i)
			x -= 1
			y += 1

	else: # ↗
		_list[y][x] = str(i)
		x += 1
		y -= 1
		_dir = 'NE'

if input_num == 1:
	print('1')
	
else:
	for row in _list:
		print(' '.join(row))