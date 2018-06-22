def max1(a, b):
	if a > b:
		return a
	else:
		return b

def max(a, b, c):
	return max1(max1(a, b), c)


def maxSubArraySum(arr, low, high):
	#print(arr)
	#print("LOW: ",low,"  HIGH: ",high)
	if(low == high):
		return arr[low]
	mid = (low + high) // 2

	return max(maxSubArraySum(arr, low, mid), maxSubArraySum(arr, mid + 1, high), maxCrossingSum(arr, low, mid, high))


def maxCrossingSum(arr, low, mid, high):
	sum = 0
	max_left = 0
	max_right = 0
	i = mid
	j = mid + 1
	while i >= low:
		sum += arr[i]
		if sum > max_left:
			max_left = sum
		i -= 1
	sum = 0
	while j <= high:
		sum += arr[j]
		if sum > max_right:
			max_right = sum
		j += 1

	return max_left + max_right

#l = [-2,-3,4,-1,-2,1,5,-3]
l = [4,-2,6,-10,8,1]
print(maxSubArraySum(l, 0, len(l) - 1))
