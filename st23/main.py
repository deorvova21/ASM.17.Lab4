from .catalog import *

def stop():
    return 1

def main():
    catalog = Catalog()
    MENU = [
        ['Добавить новый автомобиль', catalog.add_new],
        ['Добавить подержанный автомобиль', catalog.add_used],
        ['Показать каталог', catalog.show_catalog],
        ['Редактировать каталог', catalog.edit_catalog],
        ['Удалить автомобиль', catalog.delete_auto],
        ['Очистить каталог', catalog.clear_catalog],
        ['Сохранить каталог', catalog.save_catalog],
        ['Загрузить каталог', catalog.load_catalog],
        ['Выход',stop]
    ]

    while True:
        print('--Меню--')
        i = 0
        for item in MENU:
            print("{0}. {1}".format(i, item[0]))
            i += 1
        try:
            option = int(input("\nВвод: "))
            if option != 8:
                MENU[option][1]()
            else:
                return
        except:
            print('Неверный ввод\n')
        
if __name__ == '__main__':
    main()
