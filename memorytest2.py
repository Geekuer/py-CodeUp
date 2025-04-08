# [1430]

dummy = input()

num_input = input().rstrip()
# a_list = []
a_dict = {}
current_num = ''

for num in num_input:
	if num != ' ':
		current_num += num
	
	else:
		# a_list.append(current_num)
		a_dict[current_num] = True
		current_num = ''

else:
	# a_list.append(current_num)
	a_dict[current_num] = True

# ------------------------------

dummy = input()

question = input().rstrip()
q_list = []
current_num = ''

for num in question:
	if num != ' ':
		current_num += num
	
	else:
		q_list.append(current_num)
		current_num = ''

else:
	q_list.append(current_num)

# ------------------------------

for num in q_list:
	# if num in a_list:
	if num in a_dict:
		print(1, end=' ')

	else:
		print(0, end=' ')