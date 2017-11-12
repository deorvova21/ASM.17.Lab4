from .customers import *

def load(customers):
    customers.load()
    print("Загружено\n")

def send(customers):
    customers.send()
    print("Отправлено\n")


def exit(customers):
    return

customers = Customers()

def main():    
    print("Меню")
    print("1. Загрузить из файла")    
    print("2. Отправить по http")
    print("0. Выход")
    choice = input(" >>  ")
    menu(choice)

 
def menu(choice):
    try:
        menu_actions[choice](customers)
    except KeyError:
        print("Ошибка ввода\n")
    if choice != '0':       
        menu_actions['main']()


menu_actions = {
    'main': main,
    '1': load,
    '2': send,
    '0': exit,
}
 
if __name__ == "__main__":
    main()