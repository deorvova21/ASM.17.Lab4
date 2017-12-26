from .Car_company import *

car_company=Car_company()


def main():
    MENU = [
        ['Load from file', car_company.loading],
        ['Write in database', car_company.store],
        ['Clear database', car_company.delete],
        ['Add car', car_company.add_stu],
        ['Show', car_company.show],
        ['Delete', car_company.dell],
        ['Edit', car_company.change],
        ['Add driver', car_company.add_sta],
        ['Exit']
        ]
    try:
        while True:
            i = 0
            for item in MENU:
                    print(i, item[0])
                    i += 1
            print("------------------------------")
            opt = int(input('Enter number of operation: '))
            if opt!=8:
                MENU[opt][1]()
            else:
                break
    except:
        print('exception')
