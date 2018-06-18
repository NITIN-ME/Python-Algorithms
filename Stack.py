class Empty(Exception):
	def __init__(self, message):
		print(message)

class ArrayStack:
	def __init__(self):
		self._data = []

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self._data) == 0

	def push(self, e):
		self._data.append(e)

	def top(self):
		try:
			if(self.is_empty()):
				raise Empty("Stack is empty")
			return self._data[-1]
		except Empty as e:
			pass

	def pop(self):
		try:
			if(self.is_empty()):
				raise Empty("Stack is empty")
			return self._data.pop()
		except Empty as e:
			pass


S = ArrayStack( ) # contents: [ ]
print(S.top())
S.push(5) # contents: [5]
S.push(3) # contents: [5, 3]
print(len(S)) # contents: [5, 3]; outputs 2
print(S.pop( )) # contents: [5]; outputs 3
print(S.is_empty()) # contents: [5]; outputs False
print(S.pop( )) # contents: [ ]; outputs 5
print(S.is_empty()) # contents: [ ]; outputs True
S.push(7) # contents: [7]
S.push(9) # contents: [7, 9]
print(S.top( )) # contents: [7, 9]; outputs 9
S.push(4) # contents: [7, 9, 4]
print(len(S)) # contents: [7, 9, 4]; outputs 3
print(S.pop( )) # contents: [7, 9]; outputs 4
S.push(6) # contents: [7, 9, 6]
print(S.top()) # contents: [7, 9, 6]; outputs 6
S.push(7) # contents: [7, 9, 6, 7]
print(len(S)) # contents: [7, 9, 6, 7]; outputs 4
