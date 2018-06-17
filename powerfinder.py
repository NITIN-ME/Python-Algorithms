def power1(x, n):
	final = 1
	for i in range(n):
		final *= x
	return final

def power2(x, n):
	if n == 0:
		return 1
	else:
		return power2(x, n - 1) * x

def power3(x, n):
	if n == 0:
		return 1
	elif(n % 2 == 0):
		return power3(x*x, n//2)
	else:
		return power3(x*x, n//2) * x


while True:
	num = int(input("Enter the number: "))
	powr = int(input("Enter exponent: "))
	print(power1(num, powr))
	print(power2(num, powr))
	print(power3(num, powr))
