"""
__init__
__len__
is_empty
first
last
dequeue
enqueue
rotate
"""

class Empty(Exception):
	def __init__(self, message):
		print(message)

class CircularQueue:

	class _Node:
		__slots__ = '_element', '_next'

		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		return self._tail._next._element

	def last(self):
		return self._tail._element

	def dequeue(self):
		try:
			if(self.is_empty()):
				raise Empty("Queue is empty")
			oldhead = self._tail._next
			if(self._size == 1):
				self._tail = None
			else:
				self._tail._next = oldhead._next
			self._size -= 1
			return oldhead._element
		except Empty as e:
			pass

	def enqueue(self, e):
		newnode = self._Node(e, None)
		if(self._size == 0):
			newnode._next = newnode
		else:
			oldnode = self._tail._next
			self._tail._next = newnode
			newnode._next = oldnode
		self._tail = newnode
		self._size += 1

	def rotate(self):
		if(self._size > 0):
			self._tail = self._tail._next

	def show(self):
		if(not self.is_empty()):
			haha = self._tail._next
			for i in range(self._size):
				print(haha._element, end ="  ")
				haha = haha._next
			print()


q = CircularQueue()
q.dequeue()
print(q.is_empty())
q.enqueue(5)
q.show()
q.enqueue(7)
q.show()
print("Size: ",end = "")
print(len(q))
print(q.is_empty())
q.show()
print(q.first())
print(q.last())
print("Size: ",end = "")
print(len(q))
q.enqueue(8)
q.enqueue(9)
print(q.first())
print(q.last())
print(q.is_empty())
q.show()
print("Size: ",end = "")
print(len(q))
q.enqueue(10)
q.show()
print("Size: ",end = "")
print(len(q))
q.enqueue(11)
q.enqueue(12)
q.show()
print("Size: ",end = "")
print(len(q))
print("--------------------------------")
q.dequeue()
q.show()
print(q.first())
print(q.last())
print("Size: ",end = "")
print(len(q))
q.dequeue()
q.show()
q.enqueue(13)
q.show()
print(q.first())
print(q.last())
print("Size: ",end = "")
print(len(q))
print(q.is_empty())
print(not q.is_empty())
