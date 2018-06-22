from random import randint

def QuickSort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)
		QuickSort(arr, low, pi - 1)
		QuickSort(arr, pi + 1, high)

def partition(arr, low, high):
	pivot = randint(low, high)
	i = low
	arr[i], arr[pivot] = arr[pivot], arr[i]
	number = arr[low]
	#print(arr)
	#print("PIVOT: ", number)
	i += 1
	j = i
	while i <= high:
		if arr[i] < number:
			arr[j], arr[i] = arr[i], arr[j]
			i += 1
			j += 1
		else:
			i += 1
	arr[low], arr[j-1] = arr[j-1], arr[low]
	return j-1

a = [5,1,9,4,3,6,2,0,11,99,87]
print(a)
QuickSort(a, 0, len(a) - 1)
#print(partition(a,0,len(a)-1))
print(a)
