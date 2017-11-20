from st17.TransHTTP import TransHTTP
import pickle

def main():
    try:
        th = TransHTTP('http://localhost:81/cgi-bin/lab3.py', 17)
        with open('st17/menu.pkl', 'rb') as f:
            menu = pickle.load(f)

        for i in menu:
            th.SendDish(i)
            
    except Exception as e:
        print(e, '<br>')

if __name__ == "__main__":
    main()
