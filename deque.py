"""
len(D)
D.is_empty()
D.add_first()
D.add_last()
D.delete_first()
D.delete_last()
D.first() 
D.last()
"""

class Empty(Exception):
	def __init__(self, message):
		print(message)

class Deque:

	MAX_CAPACITY = 10

	def __init__(self):
		self._data = [None] * Deque.MAX_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def add_first(self, e):
		if(len(self._data) == self._size):
			self._resize(2 * len(self._data))
		self._data[(self._front - 1) % len(self._data)] = e
		self._size += 1
		self._front -= 1

	def add_last(self, e):
		if(len(self._data) == self._size):
			self._resize(2 * len(self._data))
		self._data[self._front + self._size] = e
		self._size += 1

	def first(self):
		try:
			if(self._size == 0):
				raise Empty("Deque is empty")
			return self._data[self._front]
		except Empty as e:
			pass

	def last(self):
		try:
			if(self._size == 0):
				raise Empty("Deque is empty")
			return self._data[self._front + self._size - 1]
		except Empty as e:
			pass

	def delete_first(self):
		try:
			if(self._size == 0):
				raise Empty("Deque is empty")
			self._size -= 1
			self._front  = (self._front + 1) % len(self._data)
		except Empty as e:
			pass

	def delete_last(self):
		try:
			if(self._size == 0):
				raise Empty("Deque is empty")
			self._size -= 1
		except Empty as e:
			pass

d = Deque()
print(d.is_empty())
d.delete_last()
d.delete_first()
d.add_first(7) # [7]
d.add_first(6) # [6, 7]
d.add_last(8) # [6, 7, 8]
print(d.is_empty())
print("Size: ",end ="")
print(len(d))
print(d.first())
print(d.last())
d.delete_last() # [6, 7]
print("Size: ",end ="")
print(len(d))
print(d.first())
print(d.last())
d.add_first(1) # [1, 6, 7]
d.add_first(2) # [2, 1, 6, 7]
d.add_last(61) # [2, 1, 6, 7, 61]
d.add_last(71) # [2, 1, 6, 7, 61, 71]
print(d.is_empty())
print("Size: ",end ="")
print(len(d))
print(d.first())
print(d.last())
