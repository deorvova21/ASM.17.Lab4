from .Company import *

def main():
    company = Company()
    MENU = [
        ["Добавить сотрудника", company.Add_Worker],
        ["Добавить бывшего сотрудника", company.Add_Fired],
        ["Вывести список", company.Show_List],
        ["Записать список в файл", company.Write_File],
        ["Считать список из файла", company.Read_File],
        ["Очистить список", company.Clear_List],
        ["Редактровать объект", company.Edit_Worker],
        ["Удалить элемент", company.Delete_Worker],
        ["Выход"]
    ]

    while True:
        print('--Меню--')
        i = 0
        for item in MENU:
            print("{0}. {1}".format(i, item[0]))
            i += 1
        try:
            num = int(input("\nВвод: "))
            if num != 8:
                MENU[num][1]()
            else:
                return
        except:
            print('Неверный ввод\n')
        
if __name__ == '__main__':
    main()
