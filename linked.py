"""
use  __slots__
__init__
__len__
is_empty
push
top
pop
"""

class Empty(Exception):
	def __init__(self, message):
		print(message)

class LinkedStack:

	class _Node:
		__slots__ = '_element', '_next'

		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._head = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def push(self, e):
		self._head = self._Node(e, self._head)
		self._size += 1

	def top(self):
		try:
			if(self._size == 0):
				raise Empty("Stack is empty")
			result = self._head._element
			return result
		except Empty as e:
			pass

	def pop(self):
		try:
			if(self._size == 0):
				raise Empty("Stack is empty")
			answer = self._head._element
			self._head = self._head._next
			self._size -= 1
			return answer
		except Empty as e:
			pass


l = LinkedStack()
print(l.top())
print(l.pop())
l.push(5)
l.push(7)
l.push(8)
l.push(9)
l.push(10)
print("Size is: ", end = "")
print(len(l))
print(l.top())
print(l.pop())
print("Size is: ", end = "")
print(len(l))
print(l.top())
print(l.pop())
print("Size is: ", end = "")
print(len(l))
print(l.top())
print(l.pop())
print("Size is: ", end = "")
print(len(l))
print(l.top())
print(l.pop())
print("Size is: ", end = "")
print(len(l))
print(l.top())
print(l.pop())
print("Size is: ", end = "")
print(len(l))
print(l.top())
print(l.pop())
