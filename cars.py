# Customer selects desired vehicle, specifies rental period, and makes a reservation.
from faker import Faker
import random
import csv
from datetime import datetime, timedelta



fake = Faker()

num_cars = 20
mark = ["BMW", "Audi", "Mazda", "Toyota", "Ford"]
fuel_type = ["Gasoline", "Dizel", "Gas", "Electro"]
gearbox = ["mechanical", "automatic"]
counter = 1

class Clinets(object):
    def __init__(self, name, phone, email, passport, client_id):
        self.name = name
        self.phone = phone
        self.email = email
        self.passport = passport
        self.client_id = client_id

class Cars(object):
    wheels = 4
    catalog = []

    def __init__(self, mark, model, cost, speed, years, fuel_type, gearbox, car_type, car_id):
        self.mark = mark
        self.model = model
        self.cost = cost
        self.speed = speed
        self.years = years
        self.fuel_type = fuel_type
        self.gearbox = gearbox
        self.car_type = car_type
        self.car_id = car_id

def database_cars():
    global counter
    data = []
    for i in range(num_cars):
        car = {
            "mark": random.choice(mark),
            "model": fake.word(),
            "cost": fake.random_int(min=100, max=2000),
            "speed": fake.random_int(min=90, max=260),
            "years": fake.random_int(min=1, max=20),
            "fuel_type": random.choice(fuel_type),
            "gearbox": random.choice(gearbox),
            "car_type": fake.word(),
            "car_id": str(counter)

        }
        data.append(car)
        counter += 1
    return data

def save_csv(name, data):
    with open(name, 'w', newline='') as csvfile:
        fieldnames = ["mark", "model", "cost", "speed", "years", "fuel_type", "gearbox", "car_type", "car_id"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    employee_data_list = database_cars()  # data generation
    save_csv("DataBaseCars.csv", employee_data_list)  # write data to file csv

def print_cars():
    for car in database_cars():
        print(car)
print("Catalog:")
print_cars()

def select_car(car_id): # for selecting a car by ID
    cars = database_cars()
    for car in cars:
        if car["car_id"] == car_id:
            return car

reservation_lst = []
class Reservation:
    def __init__(self, date_of_reservation, end_of_reservation, cost, client_id, car_id):
        self.date_of_reservation = date_of_reservation
        self.end_of_reservation = end_of_reservation
        self.cost = cost
        self.client_id = client_id
        self.car_id = car_id


    def booking_car (client_id, car_id):
        if car_id in reservation_lst:
            print("car already booked")
        elif car_id not in reservation_lst:
            reservation_lst.append(car_id)
            print("car booked!")
        else:
            raise ValueError("car is not in catalog")


    def create_future_date_dict():
        start_time = datetime.now()
        end_time = start_time + timedelta(days=30)
        result = {
            "start": start_time.strftime("%Y-%m-%d"),
            "end": end_time.strftime("%Y-%m-%d")
        }

        return result

    future_date_dict = create_future_date_dict()
    print(future_date_dict)
