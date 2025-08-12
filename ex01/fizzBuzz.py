def fizzBuzz():
	for x in range(1, 101):
		if x % 3 == 0 and x % 5 == 0:
			print("FizzBuzz")
		elif x % 3 == 0:
			print("Fizz")
		elif x % 5 == 0:
			print("Buzz")
		else:
			print(x)

def fizzBuzzBonus(bonus_dict):
	for x in range(1, 101):
		valueFound = False
		for key, value in bonus_dict.items():
			if x % int(key) == 0:
				valueFound = True
				print(value, end="")
		if not valueFound:
			print(x)
		else:
			print()

if __name__ == "__main__":
	bonus_dict = {
		'4': 'Fizz',
		'9': 'Buzz',
		'12': 'Lazz'
	}
	fizzBuzz()
	print("BONUS:")
	fizzBuzzBonus(bonus_dict)