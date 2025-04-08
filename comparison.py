# [1440]

num = int(input())

nums = list(map(int, input().split()))

for i in range(num):
	print(f'{i + 1}:', end=' ')

	for j in range(i): 
		if nums[i] > nums[j]:
			print('>', end=' ')
		
		elif nums[i] < nums[j]:
			print('<', end=' ')

		else:
			print('=', end=' ')

	for j in range(i + 1, num):
		if nums[i] > nums[j]:
			print('>', end=' ')
		
		elif nums[i] < nums[j]:
			print('<', end=' ')

		else:
			print('=', end=' ')

	print()