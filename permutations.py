def joiner(l):
	return ''.join(l)

def permutations(slist, start, end):
	if start == end:
		print(joiner(slist))
	else:
		for k in range(start, end + 1):
			slist[k], slist[start] = slist[start], slist[k]
			permutations(slist, start + 1, end)
			slist[k], slist[start] = slist[start], slist[k]

a = "fun"

permutations(list(a), 0, len(a) - 1)
