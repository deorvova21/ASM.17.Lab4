﻿import st00.main
import st01.main
import st22.main
import st26.main
import st38.main
#	добавить импорт своего модуля по шаблону
#	import st<номер по журналу>.main

MENU = [
        ["[00] Образец", st00.main.main],
        ["[01] Абдуллатипова", st01.main.main],
        ["[22] Ишмаметьев", st22.main.main],
        ["[26] Ларионов", st26.main.main],
        ["[38] Солопеева", st38.main.main],
#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<номер по журналу>] <Фамилия>", <ссылка на функцию>],
	]

def menu():
	print("------------------------------")
	for i, item in enumerate(MENU):
		print("{0:2}. {1}".format(i, item[0]))
	print("------------------------------")
	return int(input())

try:
	while True:
		MENU[menu()][1]()
except:
	print("bye")
