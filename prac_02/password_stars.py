"""Password check program"""
password = input("Please enter password: ")
while len(password) < 8:
    print("Invalid password")
    password = input("Please enter password: ")
print("*" * len(password))
