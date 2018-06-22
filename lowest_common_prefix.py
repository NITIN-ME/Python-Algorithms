def magic(s1, s2):
	n1 = len(s1)
	n2 = len(s2)
	k = min(n1,n2)
	s = ""
	#print("k: ",k)
	for i in range(k):
		#print("i: ",i)
		if s1[i] != s2[i]:
			break
		s += s1[i]
	return s



def divideAndConquer(l, low, high):
	if(low == high):
		return l[high]
	if(high > low):
		mid = (low + high) // 2
		str1 = divideAndConquer(l, low, mid)
		str2 = divideAndConquer(l, mid+1, high)
		return magic(str1, str2)

l = ["Nitin", "Niti","Nishant", "Nilesh","Nine"]

print(divideAndConquer(l,0, len(l)-1))
