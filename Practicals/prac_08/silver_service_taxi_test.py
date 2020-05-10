from Practicals.prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Prius the Fancy", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print(my_taxi.get_fare())


main()
