# [1285]

# 단, 우선순위는 따지지 않고 왼쪽에서 부터 차례대로 계산하고, 모든 계산은 정수형 계산으로 처리한다.
# 3+3-3*3/3=

cal = input()
total = 0
current = ''
operator = ''
isfirst = True

for char in cal:
	if char.isdigit():
		current += char

	else:
		if isfirst:
			total += int(current)
			isfirst = False
			current = ''
			operator = char
			continue

		if operator == '+':
			total += int(current)
		
		elif operator == '-':
			total -= int(current)

		elif operator == '*':
			total *= int(current)

		elif operator == '/':
			total = int(total / int(current))

		current = ''
		operator = char

print(total)