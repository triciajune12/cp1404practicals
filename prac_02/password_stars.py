def main():
    """Password check program"""
    password = get_password()
    print_stars(password)


def print_stars(password):
    print("*" * len(password))


def get_password():
    password = input("Please enter password: ")
    while len(password) < 8:
        print("Invalid password")
        password = input("Please enter password: ")
    return password


main()
