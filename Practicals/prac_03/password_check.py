MINIMUM_LENGTH = 6


def main():
    password = get_user_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_user_password(minimum_length):
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(password):
    print('*' * len(password))


main()
