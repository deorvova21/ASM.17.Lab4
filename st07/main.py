from .Group import *

def main():
    group = Group()

    MENU = [
        ["Добавить студента", group.AddStudent],
        ["Добавить старшекурсника", group.AddUndergraduate],
        ["Вывести список на экран", group.ShowList],
        ["Записать список в файл", group.WriteToFile],
        ["Считать список из файла", group.ReadFromFile],
        ["Очистить список", group.ClearList],
        ["Редактировать элемент", group.ChangeStudent],
        ["Удалить элемент списка", group.DeleteStudent],
        ["Выход"]
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
