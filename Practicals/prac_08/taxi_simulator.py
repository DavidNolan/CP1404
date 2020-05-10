from Practicals.prac_08.silver_service_taxi import SilverServiceTaxi
from Practicals.prac_08.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius 1", 100), SilverServiceTaxi("Prius the Fancy", 120, 1), SilverServiceTaxi("Fancy Limo", 80, 5)]
    chosen_taxi = None
    total_bill = 0
    print("Let's Drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            chosen_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            taxi_drive(chosen_taxi, total_bill)
            print("Bill to date: {:.2f}".format(total_bill))
        else:
            print("Invalid option")

        print(MENU)
        menu_choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now: ")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def taxi_drive(chosen_taxi, total_bill):
    chosen_taxi.start_fare()
    distance_to_drive = float(input("Drive how far? "))
    chosen_taxi.drive(distance_to_drive)
    trip_cost = chosen_taxi.get_fare()
    total_bill = + trip_cost
    print("Your {} trip cost you ${:.2f}".format(chosen_taxi, trip_cost))


main()
