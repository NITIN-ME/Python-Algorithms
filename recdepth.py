import sys
sys.setrecursionlimit(1000000)
def fact(n):
	if(n == 0 or n == 1):
		return 1
	else:
		return n * fact(n - 1)

print(fact(1000))
