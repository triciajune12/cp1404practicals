COLOURS_TO_CODE = {"black": "#000000", "electric blue": "#7df9ff",
                   "caribbean green": "#00cc99", "fuzzy wuzzy": "87421f",
                   "lemon curry": "#cca01d", "macaroni and cheese": "#ffbd88",
                   "mango tango": "#ff8243", "piggy pink": "#fddde6",
                   "school bus yellow": "#ffd800", "granny smith apple": "#a8e4a0"}
print(COLOURS_TO_CODE)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in COLOURS_TO_CODE:
        print(f"The colour code for \"{colour_name}\" is {COLOURS_TO_CODE.get(colour_name)}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
