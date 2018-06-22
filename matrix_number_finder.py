def matrixFinder(mat, elem):
	i = 0
	j = len(mat) - 1
	while(i < len(mat) and j >= 0):
		if mat[i][j] == elem:
			print("i: ",i," j: ",j)
			return
		elif mat[i][j] > elem:
			j -= 1
		else:
			i+= 1
	print("Number not found")


mat = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]

for i in range(len(mat)):
	for j in range(len(mat[0])):
		print(mat[i][j], end ="  ")
	print()

print("--------------------------------------------")

while True:
	num = int(input("Enter the number you wanna find: "))
	matrixFinder(mat, num)
