def kadane(l):
	low = 0
	high = len(l) - 1
	max_until_now = 0
	max_now = 0
	for i in range(len(l)):
		max_now += l[i]
		if(max_now > max_until_now):
			max_until_now = max_now
		if(max_now < 0):
			max_now = 0
	return max_until_now

l = [-2,-3,4,-1,-2,1,5,-3]
#l = [4,-2,6,-10,8,1]
print(kadane(l))
