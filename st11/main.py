from .items import *

It = Items()

list = [
["Считать из файла список", It.read_file],
["Отправить список на сервер", It.send]
]

def main():
        try:
                i=1
                print("Введите номер действия")
                for o in list:
                        print(i, o[0])
                        i+=1
                print("Для возврата в предыдуще меню нажмите 0")    
                k = int(input())
                if (k==0): return
                print("")
                list[k-1][1]()
                print("")
                main()
        except:
                print("Введено некорректное значение")
                main()



                
                        
                
                        
