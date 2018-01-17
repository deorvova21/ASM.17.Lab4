from .classContainerFIle import classContainer

def main():
    i=0
    classContainerExemplar = classContainer()

    while i!='2':
        print("1-Импоритровать\n2 -Выход ")
        i=input()
        if i=='1':
            classContainerExemplar.importFromPickle()


if __name__=="__main__":
    main()


