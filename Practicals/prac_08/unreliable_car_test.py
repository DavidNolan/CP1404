from Practicals.prac_08.unreliable_car import UnreliableCar


def main():
    """Test Taxi class."""
    my_unreliable_car = UnreliableCar("The Broken 01", 100, 50)
    my_unreliable_car.drive(40)
    print(my_unreliable_car)
    my_unreliable_car.drive(100)
    print(my_unreliable_car)


main()
