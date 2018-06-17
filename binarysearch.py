def finder(arr, num):
	start = 0
	end = len(arr) - 1
	while start <= end:
		mid = (start + end)//2
		if(arr[mid] == num):
			return mid
		elif(arr[mid] > num):
			end = mid - 1
		else:
			start = mid + 1
	return -1

def binfinder(arr, num, start, end):
	if(start <= end):
		mid = (start + end)//2
		if(arr[mid] == num):
			return mid
		elif(arr[mid] > num):
			return binfinder(arr, num, start, mid - 1)
		else:
			return binfinder(arr, num, mid + 1, end)
	else:
		return -1


arr = [11, 22, 33, 44, 55, 66, 77]

print(arr)
while True:
	num = int(input("Enter the number you wanna find: "))
	print(finder(arr, num))
	print(binfinder(arr, num, 0, len(arr) - 1))
