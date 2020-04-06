COLOUR_NAME_TO_HEXADECIMAL = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4",
                              "azure1": "#f0ffff", "beige": "#f5f5dc", "black": "#000000", "BlanchedAlmond": "#ffebcd",
                              "blue1": "#ffebcd",
                              "brown": "#a52a2a", "chartreuse1": "#7fff00"}

colour_name = input("Enter Colour Name: ")
while colour_name != "":
    if colour_name in COLOUR_NAME_TO_HEXADECIMAL:
        print("The code for {} is {}".format(colour_name,
                                             COLOUR_NAME_TO_HEXADECIMAL.get(colour_name)))
    else:
        print("Invalid")
    colour_name = input("Enter Colour Name: ")
print("Have a nice day.")
