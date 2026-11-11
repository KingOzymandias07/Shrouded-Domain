def is_numbered(text):
	number = text[-5]
	try:
		number = int(number)
		end = text[-5:]
	except ValueError:
		end = text[-4:]

	print(end)

def main():
	text = "yes.txt"
	while text != "quit":
		text = input("> ")
		is_numbered(text)

main()