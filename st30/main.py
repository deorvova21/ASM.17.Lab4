from st30.Loader import Loader
from st30.function import *


def main():
	loader = Loader()
	menu = {
		"1": ['save to base', loader.save],
		"2": ['exit']
	}
	show_menu(menu)
	while (True):
		item = input('Select menu item\n')
		if str.lower(item) == "2":
			break
		for i in menu:
			if ('menu' == str.lower(item)):
				show_menu(menu)
				break
			elif str.lower(i) == str.lower(item):
				menu[i][1]()


if __name__ == "__main__":
	main()
