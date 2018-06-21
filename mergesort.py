def MergeSort(l, start, end):
	if start < end:
		mid = (start + end) // 2
		MergeSort(l, start, mid)
		MergeSort(l, mid + 1, end)
		Merge(l, start, mid, end)

def Merge(l, start, mid, end):
	left = l[start:mid+1]
	right = l[mid+1:end+1]
	final = []
	lsize = len(left)
	rsize = len(right)
	i = 0
	j = 0
	while i < lsize and j < rsize:
		#print("i: ",i,"  j: ",j)
		if left[i] < right[j]:
			final.append(left[i])
			i += 1
		else:
			final.append(right[j])
			j += 1
	while i < lsize:
		final.append(left[i])
		i += 1
	while j < rsize:
		final.append(right[j])
		j += 1
	l[start:end+1] = final


#l = [3,2,1,4,6,5]
l = [5,4,1,8,7,2,6,3]
MergeSort(l, 0, len(l) - 1)
print(l)
