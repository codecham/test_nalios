def checkAllRealNumer(arr):
	return all(isinstance(number, (int, float)) for number in arr)

def sumArray(arr):
	result = 0
	if not checkAllRealNumer(arr):
		raise TypeError("sumArray(): Array must contains only numbers")
	for number in arr:
		result += number
	print(result)

if __name__ == "__main__":

	#TEST WITH VALID ARRAY
	sumArray([])
	sumArray([1, 3, 5, 6])
	sumArray([1, 2.1, 3, 4, 3.3])
	
	# TEST WITH BAD VALUE IN ARRAY 
	# sumArray([1, 2, 'z', 3])