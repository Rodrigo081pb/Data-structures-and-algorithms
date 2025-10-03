class RouteTrieNode:
	def __init__(self):
		self.children = {}
		self.handler = None

	def insert(self, part):
		if part not in self.children:
			self.children[part] = RouteTrieNode()

class RouteTrie:
	def __init__(self, root_handler):
		self.root = RouteTrieNode()
		self.root.handler = root_handler

	def insert(self, parts, handler):
		node = self.root
		for part in parts:
			node.insert(part)
			node = node.children[part]
		node.handler = handler

	def find(self, parts):
		node = self.root
		for part in parts:
			if part in node.children:
				node = node.children[part]
			else:
				return None
		return node.handler

class Router:
	def __init__(self, root_handler, not_found_handler=None):
		self.trie = RouteTrie(root_handler)
		self.not_found_handler = not_found_handler

	def add_handler(self, path, handler):
		parts = self.split_path(path)
		self.trie.insert(parts, handler)

	def lookup(self, path):
		parts = self.split_path(path)
		if len(parts) == 0:
			result = self.trie.root.handler
		else:
			result = self.trie.find(parts)
		if result is None:
			return self.not_found_handler
		return result

	def split_path(self, path):
		# Remove barra inicial/final e divide, ignorando strings vazias
		return [part for part in path.strip('/').split('/') if part]

# Testes
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'
