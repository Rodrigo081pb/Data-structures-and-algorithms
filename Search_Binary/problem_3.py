import sys
import heapq

class Node:
	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None
	def __lt__(self, other):
		return self.freq < other.freq

def build_tree(data):
	if not data:
		return None
	freq = {}
	for char in data:
		freq[char] = freq.get(char, 0) + 1
	heap = [Node(char, f) for char, f in freq.items()]
	heapq.heapify(heap)
	while len(heap) > 1:
		left = heapq.heappop(heap)
		right = heapq.heappop(heap)
		merged = Node(None, left.freq + right.freq)
		merged.left = left
		merged.right = right
		heapq.heappush(heap, merged)
	return heap[0]

def build_codes(node, prefix='', code_map=None):
	if code_map is None:
		code_map = {}
	if node:
		if node.char is not None:
			code_map[node.char] = prefix or '0'
		else:
			build_codes(node.left, prefix + '0', code_map)
			build_codes(node.right, prefix + '1', code_map)
	return code_map

def huffman_encoding(data):
	tree = build_tree(data)
	codes = build_codes(tree)
	encoded = ''.join(codes[c] for c in data) if data else ''
	return encoded, tree

def huffman_decoding(data, tree):
	if not tree or not data:
		return ''
	decoded = []
	node = tree
	for bit in data:
		node = node.left if bit == '0' else node.right
		if node.char is not None:
			decoded.append(node.char)
			node = tree
	return ''.join(decoded)

if __name__ == "__main__":
	a_great_sentence = "The bird is the word"
	print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
	print(f"The content of the data is: {a_great_sentence}")
	encoded_data, tree = huffman_encoding(a_great_sentence)
	print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data or '0', base=2))}")
	print(f"The content of the encoded data is: {encoded_data}")
	decoded_data = huffman_decoding(encoded_data, tree)
	print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
	print(f"The content of the decoded data is: {decoded_data}")

	# Teste 1: String vazia
	test1 = ""
	enc1, tree1 = huffman_encoding(test1)
	print(f"Teste 1 - vazio: {enc1}, decodificado: '{huffman_decoding(enc1, tree1)}'")

	# Teste 2: String nula
	test2 = None
	enc2, tree2 = huffman_encoding(test2)
	print(f"Teste 2 - nulo: {enc2}, decodificado: '{huffman_decoding(enc2, tree2)}'")

	# Teste 3: String muito grande
	test3 = "A" * 10000
	enc3, tree3 = huffman_encoding(test3)
	print(f"Teste 3 - grande: tamanho codificado={len(enc3)}, decodificado igual? {huffman_decoding(enc3, tree3) == test3}")
