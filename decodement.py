# [1284]

# n을 두 소수의 곱으로 나타낼 수 있으면 두 수를 오름차순으로 출력한다.
# (단, 가능한 소수 중 가장 작은 소수와의 곱으로 나타낸다.)
# 하고, 그렇지 않으면 "wrong number"를 출력한다.

num = int(input())

def issosu (n):
	if n < 2:
		return False
	
	for i in range(2, n):
		if n % i == 0:
			return False
	
	return True

if issosu(num):
	print('wrong number')

else:
	exist = False

	for i in range(2, num + 1):
		if (num / i) % 1 == 0: # 약수라면
			if issosu(i) and issosu(int(num / i)):
				print(i, int(num / i))
				exist = True
				break
	
	if not exist:
		print('wrong number')