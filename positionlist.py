class ValueError(Exception):
	def __init__(self, message):
		print(message)

class _DoublyLinkedBase:

	class _Node:
		__slots__ = '_element', '_previous','_next'

		def __init__(self, element, previous, next):
			self._element = element
			self._previous = previous
			self._next = next

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
		newnode = self._Node(e, predecessor, successor)
		predecessor._next = newnode
		successor._previous = newnode
		self._size += 1
		return newnode

	def _delete_node(self, node):
		result = node._element
		predecessor = node._previous
		successor = node._next
		predecessor._next = successor
		successor._previous = predecessor
		node._previous = node._next = node._element = None
		self._size -= 1


class PositionalList(_DoublyLinkedBase):

	class Position:

		def __init__(self, container, node):
			self._container = container
			self._node= node


		def element(self):
			return self._node._element

		def __eq__(self, other):
			return type(self) is type(other) and self._node is other._node
		
		def __ne__(self, other):
			return not self == other

	def _validate(self, p):
		try:
			if not isinstance(p, self.Position):
				raise ValueError('Not a proper position type')
			if p._container is not self:
				raise ValueError('The container is not same')
			if p._node._next is None:
				raise ValueError('p is no longer valid')
			return p._node
		except ValueError as e:
			pass

	def _make_position(self, node):
		if node is self._header or node is self._trailer:
			return None
		else:
			return self.Position(self, node)

	def first(self):
		return self._make_position(self._header._next)

	def last(self):
		return self._make_position(self._trailer._previous)

	def before(self, p):
		node = self._validate(p)
		return self._make_position(node._previous)

	def after(self, p):
		node = self._validate(p)
		return self._make_position(node._next)

	def __iter__(self):
		current = self.first()
		while current is not None:
			yield current.element()
			current = self.after(current)

	def show(self):
		current = self.first()
		while current is not None:
			print(current.element(), end = "  ")
			current = self.after(current)
		print()

	def _insert_between(self, e, predecessor,successor):
		node = super()._insert_between(e, predecessor, successor)
		return self._make_position(node)

	def add_first(self, e):
		return self._insert_between(e, self._header, self._header._next)

	def add_last(self, e):
		return self._insert_between(e, self._trailer._previous, self._trailer)

	def add_before(self, p, e):
		original = self._validate(p)
		return self._insert_between(e, original._previous, original)

	def add_after(self, p, e):
		original = self._validate(p)
		return self._insert_between(e, original, original._next)

	def delete(self, p):
		original = self._validate(p)
		return self._delete_node(original)

	def replace(self, p, e):
		original = self._validate(p)
		old_value = original._element
		original._element = element
		return old_value


l = PositionalList()
l.add_first(7)
l.add_last(90)
l.add_first(8)
l.add_last(100)
l.add_first(9)
l.add_last(110)
l.add_first(10)
for k in l:
	print(k)
print()
l.show()
