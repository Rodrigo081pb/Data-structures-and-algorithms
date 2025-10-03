# Implementação da raiz quadrada inteira (floor) usando busca binária
def sqrt(number):
	"""
	Calculate the floored square root of a number

	Args:
	   number(int): Number to find the floored squared root
	Returns:
	   int: Floored Square Root
	"""
	if number < 0:
		return None  # Raiz quadrada não definida para negativos
	if number == 0 or number == 1:
		return number
	left, right = 0, number
	result = 0
	while left <= right:
		mid = (left + right) // 2
		if mid * mid == number:
			return mid
		elif mid * mid < number:
			result = mid
			left = mid + 1
		else:
			right = mid - 1
	return result

print("Pass" if 3 == sqrt(9) else "Fail")
print("Pass" if 0 == sqrt(0) else "Fail")
print("Pass" if 4 == sqrt(16) else "Fail")
print("Pass" if 1 == sqrt(1) else "Fail")
print("Pass" if 5 == sqrt(27) else "Fail")
