def summer(arr, start, end):
	if(start == end):
		return arr[start]
	elif(start >= end):
		return 0
	else:
		mid = (start + end)//2
		return summer(arr, start, mid) + summer(arr, mid + 1, end)

def basic(arr):
	sum = 0
	for i in arr:
		sum += i
	return sum

def tailrec(arr, n):
	if(n < 0):
		return 0
	else:
		return arr[n] + tailrec(arr, n-1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(summer(arr, 0, len(arr) - 1))
print(basic(arr))
print(tailrec(arr, len(arr) - 1))
