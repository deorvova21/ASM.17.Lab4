def is_file(value):
	try:
		open(str(value) + '.dat', 'rb')
		return True
	except FileNotFoundError:
		return False

def show_menu(menu):
	print('Menu')
	for i, item in enumerate(menu):
		print("{0} - {1}".format(item, menu[item][0]))
	print()
