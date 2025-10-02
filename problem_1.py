from collections import OrderedDict

class LRU_Cache(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.cache = OrderedDict()

	def get(self, key):
		if key in self.cache:
			self.cache.move_to_end(key)
			return self.cache[key]
		return -1

	def set(self, key, value):
		if key in self.cache:
			self.cache.move_to_end(key)
		self.cache[key] = value
		if len(self.cache) > self.capacity:
			self.cache.popitem(last=False)

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))       # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))       # returns -1 because the cache reached its capacity and 3 was the least recently used entry

## Test Case 1: Inserção de valor nulo
our_cache.set(None, 'null')
print(our_cache.get(None))    # returns 'null'

## Test Case 2: Chave vazia
our_cache.set('', 'empty')
print(our_cache.get(''))      # returns 'empty'

## Test Case 3: Valor grande
large_value = 'x' * 10000
our_cache.set('big', large_value)
print(our_cache.get('big') == large_value)  # returns True
