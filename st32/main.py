import os,pickle
__path__ = [os.path.dirname(os.path.abspath(__file__))]
from st32.Transport import Transport

def main():
    try:
        t = Transport('http://localhost:81/cgi-bin/lab3.py', 32)
        fn=input("Enter name file download");
        with open('st32/'+fn, 'rb') as f:
            office = pickle.load(f)

        for i in office:
            t.Send(i)
            
    except Exception as e:
        print(e, '<br>')


if __name__ == "__main__":
	main()





