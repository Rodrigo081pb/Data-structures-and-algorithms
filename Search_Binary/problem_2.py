import os

def find_files(suffix, path):
	"""
	Encontra todos os arquivos abaixo de path com o sufixo informado.
	"""
	if not suffix or not path or not os.path.exists(path):
		return []
	result = []
	def search(current_path):
		if os.path.isfile(current_path):
			if current_path.endswith(suffix):
				result.append(current_path)
		elif os.path.isdir(current_path):
			for entry in os.listdir(current_path):
				search(os.path.join(current_path, entry))
	search(path)
	return result

# Testes
def print_test(title, result):
	print(f"{title}: {result}")

# Teste 1: Diretório inexistente
print_test("Diretório inexistente", find_files('.c', './no_such_dir'))

# Teste 2: Sufixo vazio
print_test("Sufixo vazio", find_files('', '.'))

# Teste 3: Diretório atual (pode não ter arquivos .c)
print_test("Diretório atual", find_files('.c', '.'))

# Teste 4: Caminho para arquivo único
with open('temp_test.c', 'w') as f:
	f.write('int main() {}')
print_test("Arquivo único .c", find_files('.c', 'temp_test.c'))
os.remove('temp_test.c')
