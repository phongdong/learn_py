
def dedup(list):
	u_list = []
	for i in list:
		if i not in u_list:
			u_list.append(i)
	return u_list

def twoSum(list, target):
	newlist = []
	for i in list:
		for j in list:
			if (i + j == target):
				return (i, j)

def twoSum2(list, target):
	dic = {}
	j = 0
	for i in list:
		dic[i] = j
		j += 1
	for key, value in dic.items():
		if ((target-key) in dic):
			return ( dic[key], dic[target-key])

def reverseString(string):
	print(str[::-1])
	# print(''.join(reversed(string)))


def dedup2(list):
	list2 = []
	for i in list:
		if (i not in list2):
			list2.append(i)
	return list2

def finMin(list):
	min = list[0]
	for i in list:
		if (i< min): 
			min = i
	return min
	
list = [2,3,9,4,5,9]

# print(dedup(list))
# print(twoSum(list, 7))
# print(twoSum2(list, 7))
# reverseString("Hello world")

# print(dedup2(list))
print(finMin(list))

