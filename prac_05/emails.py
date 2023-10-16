def main():
    email_to_name = {}
    emails = input("Email: ")
    while emails != "":
        name = get_name_from_email(emails)
        name_confirmation = input(f"Is your name {name}? (Y/n) ")
        if name_confirmation.upper() != "Y" and name_confirmation != "":
            name = input("Name: ")
        email_to_name[emails] = name
        emails = input("Email: ")

    for emails, name in email_to_name.items():
        print(f"{name} ({emails})")


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
