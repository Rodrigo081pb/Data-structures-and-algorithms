def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return merge(left, right)

def merge(left, right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] > right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result.extend(left[i:])
	result.extend(right[j:])
	return result

def rearrange_digits(input_list):
	"""
	Rearranges the elements of the given array to form two numbers such that their sum is maximized.
	The numbers formed have a number of digits differing by no more than one.
	Args:
		input_list (List[int]): A list of integers
	Returns:
		Tuple[int, int]: A tuple containing two integers
	"""
	if not input_list:
		return (0, 0)
	sorted_list = merge_sort(input_list)
	num1 = []
	num2 = []
	for i, digit in enumerate(sorted_list):
		if i % 2 == 0:
			num1.append(str(digit))
		else:
			num2.append(str(digit))
	return (int(''.join(num1)), int(''.join(num2)))

def test_function(test_case):
	output = rearrange_digits(test_case[0])
	solution = test_case[1]
	if sum(output) == sum(solution):
		print("Pass")
	else:
		print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
