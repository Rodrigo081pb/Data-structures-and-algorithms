class Group(object):
	def __init__(self, _name):
		self.name = _name
		self.groups = []
		self.users = []

	def add_group(self, group):
		self.groups.append(group)

	def add_user(self, user):
		self.users.append(user)

	def get_groups(self):
		return self.groups

	def get_users(self):
		return self.users

	def get_name(self):
		return self.name

def is_user_in_group(user, group):
	"""
	Retorna True se o usuário está no grupo ou em algum subgrupo, False caso contrário.
	"""
	if user is None or group is None:
		return False
	if user in group.get_users():
		return True
	for sub_group in group.get_groups():
		if is_user_in_group(user, sub_group):
			return True
	return False

# Testes
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent))  # True
print(is_user_in_group("sub_child_user", child))   # True
print(is_user_in_group("sub_child_user", sub_child)) # True
print(is_user_in_group("no_user", parent))         # False

# Teste 1: Usuário nulo
print(is_user_in_group(None, parent))               # False

# Teste 2: Grupo nulo
print(is_user_in_group("sub_child_user", None))    # False

# Teste 3: Usuário muito grande
big_user = "x" * 10000
parent.add_user(big_user)
print(is_user_in_group(big_user, parent))           # True
