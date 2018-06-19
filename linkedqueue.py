"""
	_head
	_tail
	_size
__init__
__len__()
is_empty()
first()
last()
size()
dequeue()
enqueue()
"""

class Empty(Exception):
	def __init__(self, message):
		print(message)

class LinkedQueue:

	class _Node:
		__slots__ = '_element', '_next'

		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		return self._head._element

	def last(self):
		return self._tail._element

	def size(self):
		return self._size

	def dequeue(self):
		try:
			if(self.is_empty()):
				raise Empty("Queue is empty")
			result = self._head._element
			self._head = self._head._next
			self._size -= 1
			if(self.is_empty()):
				self._tail = None
			return result
		except Empty as e:
			pass

	def enqueue(self, e):
		newnode = self._Node(e, None)
		if(self.is_empty()):
			self._head =newnode
		else:
			self._tail._next = newnode
		self._tail = newnode
		self._size +=1

	def show(self):
		haha = self._head
		while haha:
			print(haha._element,end="  ")
			haha = haha._next


# len and size are technically same
q = LinkedQueue()
q.dequeue()
print(q.is_empty())
q.enqueue(5)
q.enqueue(7)
print("Size: ",end = "")
print(q.size())
print(q.is_empty())
print(q.first())
print(q.last())
print("Size: ",end = "")
print(q.size())
q.enqueue(8)
q.enqueue(9)
print(q.first())
print(q.last())
print(q.is_empty())
q.show()
print()
print("Size: ",end = "")
print(q.size())
q.enqueue(10)
q.show()
print()
print("Size: ",end = "")
print(q.size())
q.enqueue(11)
q.enqueue(12)
q.show()
print()
print("Size: ",end = "")
print(q.size())
print("--------------------------------")
q.dequeue()
print(q.first())
print(q.last())
print("Size: ",end = "")
print(q.size())
q.show()
print()
q.enqueue(13)
print(q.first())
print(q.last())
print("Size: ",end = "")
print(q.size())
