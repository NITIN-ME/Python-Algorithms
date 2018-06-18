class Empty(Exception):
	def __init__(self, message):
		print(message)

class ArrayQueue:
	DEFAULT_CAPACITY = 10

	def __init__(self):
		self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		try:
			if(self.is_empty()):
				raise Empty("Array is empty: ")
			return self._data[self._front]
		except Empty as e:
			pass

	def dequeue(self):
		try:
			if(self.is_empty()):
				raise Empty("Queue is empty: ")
			answer = self._data[self._front]
			self._data[self._front] = None
			self._front = (self._front + 1) % len(self._data)
			self._size -= 1
			return answer
		except Empty as e:
			pass
		

	def enqueue(self, e):
		if(self._size == len(self._data)):
			self._resize(2*len(self._data))
		current = (self._front + self._size) % len(self._data)
		self._data[current] = e
		self._size += 1

	def _resize(self, cap):
		old = self._data
		self._data = [None] * cap
		initial = self._front
		for k in range(self._size):
			self._data[k] = old[initial]
			initial = (initial + 1 ) % len(old)
		self._front = 0

q = ArrayQueue()
q.enqueue(5)
q.enqueue(3)
print(len(q))
print(q.dequeue())
print(q.is_empty())
print(q.dequeue())
print(q.is_empty())
print(q.dequeue())
print(len(q))
q.enqueue(7)
q.enqueue(9)
print(q.first())
q.enqueue(4)
print(len(q))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
print(q.dequeue())
