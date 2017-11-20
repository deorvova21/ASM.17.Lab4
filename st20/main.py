from st20.http_load import http_load
import pickle

def main():
    try:
        http = http_load('http://localhost:81/cgi-bin/lab3.py', 20)
        with open('st20/car_park.pkl', 'rb') as f:
            car_park = pickle.load(f)

        for i in car_park:
            http.load_car(i)
            
    except Exception as e:
        print(e, '<br>')

if __name__ == "__main__":
    main()
