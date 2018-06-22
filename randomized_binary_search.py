from random import randint

def RandomBinarySearch(arr, low, high, num):
	if low <= high:
		randnum = randint(low, high)
		if arr[randnum] == num:
			return randnum
		elif arr[randnum] > num:
			return RandomBinarySearch(arr, low, randnum - 1, num)
		else:
			return RandomBinarySearch(arr, randnum + 1, high, num)
	return -1

arr = [2,4,6,8,10,12,14,16,18,20]

while True:
	num = int(input('Enter the number you wanna search: '))
	print(RandomBinarySearch(arr, 0, len(arr) - 1, num))
