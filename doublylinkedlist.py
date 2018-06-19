"""
Node - element, prev, next
_header, _trailse, _next
__init__(self)
__len__(self)
is_empty(else)
_insert_between(self, e, predecessor, successor)
_delete_node(self, node)
insert_front(self, e)
insert_back(self, e)
delete_front(self)
delete_back(self)
"""

class Empty(Exception):
	def __init__(self, message):
		print(message)


class DoublyLinkedList:

	class _Node:
		__slots__ = '_element', '_previous', '_next'

		def __init__(self, element, previous, nextnode):
			self._element = element
			self._previous = previous
			self._next = nextnode

	def __init__(self):
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._previous = self._header
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def _insert_between(self, e, predecessor, successor):
		newnode= self._Node(e, predecessor, successor)
		predecessor._next = newnode
		successor._previous = newnode
		self._size += 1
		return newnode

	def _delete_node(self, node):
		predecessor = node._previous
		successor = node._next
		predecessor._next = successor
		successor._previous = predecessor
		self._size -= 1
		element = node._element
		node._previous = node._next = node._element = None
		return element

	def insert_front(self, e):
		self._insert_between(e, self._header, self._header._next)

	def insert_back(self, e):
		self._insert_between(e, self._trailer._previous, self._trailer)

	def delete_back(self):
		self._delete_node(self._trailer._previous)

	def delete_front(self):
		self._delete_node(self._header._next)

	def show(self):
		haha = self._header._next
		for i in range(self._size):
			print(haha._element,end = '  ')
			haha = haha._next
		print()

	def insert(self, e, position):
		if(position > self._size):
			print("Insert not possible")
		else:
			start = self._header
			for k in range(position):
				start = start._next
			self._insert_between(e,  start, start._next)


d = DoublyLinkedList()
d.insert_front(7)
d.show()
d.insert_front(14)
d.show()
d.insert_back(21)
d.show()
print("Size is: ",end = " ")
print(len(d))
d.insert_front(28)
d.show()
d.insert_front(35)
d.show()
d.insert_front(42)
d.show()
d.insert_front(49)
d.show()
d.insert_back(10)
d.show()
d.insert_back(20)
d.show()
d.insert_back(30)
d.show()
d.delete_front()
d.show()
d.delete_back()
d.show()
d.delete_front()
d.show()
d.delete_back()
d.show()
d.delete_back()
d.show()
d.delete_front()
d.show()
d.delete_back()
d.show()
d.delete_back()
d.show()
d.delete_front()
d.show()
d.show()
d.insert_front(10)
d.show()
d.insert_front(20)
d.show()
d.insert_front(30)
d.show()
d.insert(40,2)
d.show()
print("Size is: ",end = " ")
print(len(d))
d.insert(990,0)
d.show()
