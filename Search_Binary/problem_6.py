class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
	def __repr__(self):
		return str(self.value)

class LinkedList:
	def __init__(self):
		self.head = None
	def __str__(self):
		cur_head = self.head
		out_string = ""
		while cur_head:
			out_string += str(cur_head.value) + " -> "
			cur_head = cur_head.next
		return out_string if out_string else "Empty"
	def append(self, value):
		if self.head is None:
			self.head = Node(value)
			return
		node = self.head
		while node.next:
			node = node.next
		node.next = Node(value)
	def size(self):
		size = 0
		node = self.head
		while node:
			size += 1
			node = node.next
		return size

def union(llist_1, llist_2):
	result = LinkedList()
	seen = set()
	for llist in [llist_1, llist_2]:
		node = llist.head if llist else None
		while node:
			if node.value not in seen:
				result.append(node.value)
				seen.add(node.value)
			node = node.next
	return result

def intersection(llist_1, llist_2):
	result = LinkedList()
	if not llist_1 or not llist_2:
		return result
	set1 = set()
	node = llist_1.head
	while node:
		set1.add(node.value)
		node = node.next
	set2 = set()
	node = llist_2.head
	while node:
		set2.add(node.value)
		node = node.next
	for val in set1 & set2:
		result.append(val)
	return result

# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
for i in element_1:
	linked_list_1.append(i)
for i in element_2:
	linked_list_2.append(i)
print("União:", union(linked_list_1, linked_list_2))
print("Interseção:", intersection(linked_list_1, linked_list_2))

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_4 = [1, 7, 8, 9, 11, 21, 1]
for i in element_3:
	linked_list_3.append(i)
for i in element_4:
	linked_list_4.append(i)
print("União:", union(linked_list_3, linked_list_4))
print("Interseção:", intersection(linked_list_3, linked_list_4))

# Teste 1: Lista nula
print("União com lista nula:", union(None, linked_list_1))
print("Interseção com lista nula:", intersection(None, linked_list_1))

# Teste 2: Lista vazia
empty_list = LinkedList()
print("União com lista vazia:", union(empty_list, linked_list_1))
print("Interseção com lista vazia:", intersection(empty_list, linked_list_1))

# Teste 3: Lista muito grande
big_list_1 = LinkedList()
big_list_2 = LinkedList()
for i in range(10000):
	big_list_1.append(i)
for i in range(5000, 15000):
	big_list_2.append(i)
print("Interseção grande:", intersection(big_list_1, big_list_2))
