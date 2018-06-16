from random import randint

def getday():
	return randint(1,365)


for j in range(1,61):
	n = 100000
	count = 0
	for k in range(n):
		a = []
		for i in range(j):
			a.append(getday())
		l1 = a
		l2 = list(set(a))
		if len(l1) != len(l2):
			count += 1

	percentage = count / n * 100
	print("Percentage(",j,")  : ",percentage)
