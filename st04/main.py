from .computers import Computers

def main():
        Comp = Computers()

        list = [
	["Read from the file list", Comp.read_file],
        ["Send to server", Comp.server],
	]
        
        try:
                while True:
                        i=1
                        print("Select")
                        for o in list:
                                print(i, o[0])
                                i+=1
                        print("Press any key to exit\n")        
                        k = int(input())
                        print("------------------------------")
                        list[k-1][1]()
                        print("------------------------------")
        except:
                print("bye")
                        
                
                        
