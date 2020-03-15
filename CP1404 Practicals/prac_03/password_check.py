MINIMUM_LENGTH = 6


def main():
    user_password = get_user_password(MINIMUM_LENGTH)
    print_asterisks(user_password)


def get_user_password(minimum_length):
    user_password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(user_password) < minimum_length:
        print("Password too short")
        user_password = input("Enter password of at least {} characters: ".format(minimum_length))
    return user_password


def print_asterisks(user_password):
    print('*' * len(user_password))


main()
