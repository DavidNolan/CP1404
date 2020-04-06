import random

NUMBERS_PER_QUICK_PICK = 6
MINIMUM_LOTTERY_NUMBER = 1
MAXIMUM_LOTTERY_NUMBER = 45


def main():
    number_of_quick_picks = int(input("Enter number of quick picks: "))
    while number_of_quick_picks <= 0:
        print("That option is not valid, try again.")
        number_of_quick_picks = int(input("Enter number of quick picks"))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_QUICK_PICK):
            number = random.randint(MINIMUM_LOTTERY_NUMBER, MAXIMUM_LOTTERY_NUMBER)
            while number in quick_pick:
                number = random.randint(MINIMUM_LOTTERY_NUMBER, MAXIMUM_LOTTERY_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print("".join("{:4}".format(number) for number in quick_pick))


main()
