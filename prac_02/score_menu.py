MENU = """
    (G) - Get a valid score (must be 0-100 inclusive)
    (P) - Print result
    (S) - Show stars
    (Q)- Quit"""


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(f"Your score of {score} is {determine_category(score)}")
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid Option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_score():
    score = int(input("Enter score: "))
    return score


def determine_category(score):
    if score < 0 or score > 100:
        category = "Invalid score"
    elif score >= 90:
        category = "Excellent"
    elif score >= 50:
        category = "Passable"
    else:
        category = "Bad"
    return category


main()
