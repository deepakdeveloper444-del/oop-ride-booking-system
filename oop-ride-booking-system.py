from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, name, rate):
        self.name = name
        self.__rate = rate

    def get_rate(self):
        return self.__rate

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bike(Vehicle):

    def __init__(self):
        super().__init__("Bike", 15)

    def calculate_fare(self, distance):
        return self.get_rate() * distance


class Auto(Vehicle):

    def __init__(self):
        super().__init__("Auto", 20)

    def calculate_fare(self, distance):
        return self.get_rate() * distance


class Car(Vehicle):

    def __init__(self):
        super().__init__("Car", 25)

    def calculate_fare(self, distance):
        return self.get_rate() * distance


class LuxuryCar(Vehicle):

    def __init__(self):
        super().__init__("Luxury Car", 50)

    def calculate_fare(self, distance):
        return self.get_rate() * distance


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        return "UPI"


class Card(Payment):

    def pay(self, amount):
        return "Card"


class Cash(Payment):

    def pay(self, amount):
        return "Cash"


class Driver:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


ride_history = []
GST = 0.05


def book_ride(vehicle, driver, payment, distance):

    base_fare = vehicle.calculate_fare(distance)

    discount = 0

    if distance > 20:
        discount = base_fare * 0.10

    fare_after_discount = base_fare - discount

    gst = fare_after_discount * GST

    final_fare = fare_after_discount + gst

    print("\n========================")
    print("Ride Booked Successfully")
    print("========================")
    print("Driver :", driver.name)
    print("Rating :", driver.rating)
    print("Vehicle :", vehicle.name)
    print("Distance :", distance, "km")
    print("Rate :", vehicle.get_rate(), "/km")
    print("Base Fare :", round(base_fare, 2))
    print("Discount :", round(discount, 2))
    print("Fare :", round(fare_after_discount, 2))
    print("GST (5%) :", round(gst, 2))
    print("Total Fare :", round(final_fare, 2))
    print("Payment Mode :", payment.pay(final_fare))
    print("========================")

    ride_history.append({
        "Vehicle": vehicle.name,
        "Distance": distance,
        "Fare": round(final_fare, 2),
        "Payment Mode": payment.pay(final_fare)
    })


driver = Driver("Deepak", 5.0)

while True:

    print("\n========== Ride Booking ==========")

    print("\nAvailable Vehicles")
    print("1. Bike")
    print("2. Auto")
    print("3. Car")
    print("4. Luxury Car (BENZ)")

    choice = int(input("\nEnter Number to Select Vehicle: "))
    distance = float(input("Enter Distance (km): "))

    print("\nSelect Payment Mode")
    print("1. UPI")
    print("2. Card")
    print("3. Cash")

    pay_choice = int(input("Enter Number to Select Payment Mode: "))

    if choice == 1:
        vehicle = Bike()
    elif choice == 2:
        vehicle = Auto()
    elif choice == 3:
        vehicle = Car()
    elif choice == 4:
        vehicle = LuxuryCar()
    else:
        print("Invalid Vehicle Choice")
        continue

    if pay_choice == 1:
        payment = UPI()
    elif pay_choice == 2:
        payment = Card()
    elif pay_choice == 3:
        payment = Cash()
    else:
        print("Invalid Payment Choice")
        continue

    book_ride(vehicle, driver, payment, distance)

    again = input("\nDo you want to book another ride (Y/N): ")

    if again.lower() == "n":
        break


print("\n========== Ride History ==========")

for i, ride in enumerate(ride_history, start=1):
    print(f"\nRide {i}")
    print("Vehicle :", ride["Vehicle"])
    print("Distance :", ride["Distance"], "km")
    print("Fare :", ride["Fare"])
    print("Payment Mode :", ride["Payment Mode"])

print("\nThank You!")
