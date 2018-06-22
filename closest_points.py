from math import sqrt

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(" + str(self.x)+", "+str(self.y)+")"


def compareX(a, b):
	return a.x - b.x


def compareY(a, b):
	return a.y - b.y

def distance(a, b):
	return sqrt((a.x - b.x)*(a.x - b.x) + (a.y - b.y) * (a.y - b.y))

def bruteForce(arr ,n):
	min = 9999999
	for k in range(n):
		for j in range(k+1,n):
			s = distance(arr[k], arr[j])
			if s < min:
				min = s
	return min

def min(x, y):
	if x < y:
		return x
	else:
		return y

def stripClosest(strip, d):
	min = d
	size = len(strip)
	sortbyY(strip)
	for i in range(size):
		for j in range(i+1, size):
			if abs(strip[i].y - strip[j].y) < min:
				if(distance(strip[i], strip[j]) < min):
					min = distance(strip[i], strip[j])
	return min


def closestUtil(p):
	n = len(p)
	if(n <= 3):
		return bruteForce(p, n)
	mid = n // 2
	midpoint = p[mid]
	dl = closestUtil(p[0:mid])
	dr = closestUtil(p[mid+1:n+1])
	d = min(dl, dr)

	strip = []
	for k in range(n):
		if(abs(p[k].x - midpoint.x) < d):
			strip.append(p[k])
	return min(d, stripClosest(strip, d))

def closest(p):
	sortbyX(p)
	return closestUtil(p)

def getkeyX(item):
	return item.x

def getkeyY(item):
	return item.y

def sortbyX(p):
	return sorted(p, key = getkeyX)


def sortbyY(p):
	return sorted(p, key = getkeyY)


def show(p):
	for k in p:
		print(k, end = "   ")
	print()

a = Point(2,3)
b = Point(12,30)
c = Point(40,50)
d = Point(5,1)
e = Point(12,10)
f = Point(3,4)
g = Point(3,5)
arr = [a,b,c,g,d,e,f]
arr1 = [a,b,c,d,e,f]
print(closest(arr))
print(closest(arr1))

"""
print(bruteForce(arr, len(arr)))
print(distance(p, q))
print(abs(-5))
"""
