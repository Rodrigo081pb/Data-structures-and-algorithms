class TrieNode:
	def __init__(self):
		self.children = {}
		self.is_end_of_word = False
    
	def insert(self, char):
		if char not in self.children:
			self.children[char] = TrieNode()
		# Não retorna nada, apenas insere
    
	def suffixes(self, suffix = ''):
		results = []
		if self.is_end_of_word and suffix:
			results.append(suffix)
		for char, node in self.children.items():
			results.extend(node.suffixes(suffix + char))
		return results

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		node = self.root
		for char in word:
			node.insert(char)
			node = node.children[char]
		node.is_end_of_word = True

	def find(self, prefix):
		node = self.root
		for char in prefix:
			if char in node.children:
				node = node.children[char]
			else:
				return None
		return node
