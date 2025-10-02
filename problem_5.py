import hashlib
import datetime

class Block:
	def __init__(self, timestamp, data, previous_hash):
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calc_hash()

	def calc_hash(self):
		sha = hashlib.sha256()
		hash_str = f"{self.timestamp}{self.data}{self.previous_hash}".encode('utf-8')
		sha.update(hash_str)
		return sha.hexdigest()

	def __repr__(self):
		return f"Block(timestamp={self.timestamp}, data={self.data}, hash={self.hash[:10]}...)"

class Blockchain:
	def __init__(self):
		self.chain = []
		self.add_block("Genesis Block")

	def add_block(self, data):
		timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
		previous_hash = self.chain[-1].hash if self.chain else None
		block = Block(timestamp, data, previous_hash)
		self.chain.append(block)

	def __repr__(self):
		return '\n'.join(str(block) for block in self.chain)

# Testes
bc = Blockchain()
bc.add_block("Primeira transação")
bc.add_block("Segunda transação")
print(bc)

# Teste 1: Adicionar bloco com dados nulos
bc.add_block(None)
print("Bloco com dados nulos:", bc.chain[-1])

# Teste 2: Adicionar bloco com dados vazios
bc.add_block("")
print("Bloco com dados vazios:", bc.chain[-1])

# Teste 3: Adicionar bloco com dados muito grandes
big_data = "x" * 10000
bc.add_block(big_data)
print("Bloco com dados grandes:", bc.chain[-1])
