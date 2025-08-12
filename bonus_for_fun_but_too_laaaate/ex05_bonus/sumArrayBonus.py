def checkAllRealNumer(arr):
	return all(isinstance(number, (int, float)) for number in arr)

def sumArrayRecusive(arr):
	if len(arr) == 0:
		return 0
	if not checkAllRealNumer(arr):
		raise TypeError("sumArray(): Array must contains only numbers")
	return arr[0] + sumArrayRecusive(arr[1:])

if __name__ == "__main__":

	#TEST WITH VALID ARRAY
	print(sumArrayRecusive([]))
	print(sumArrayRecusive([1, 3, 5, 6]))
	print(sumArrayRecusive([1, 2.1, 3, 4, 3.3]))
	
	# TEST WITH BAD VALUE IN ARRAY 
	# sumArrayRecusive([1, 2, 'z', 3])