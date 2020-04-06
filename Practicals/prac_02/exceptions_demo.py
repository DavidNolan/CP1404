"""
CP1404 Practical
Answer the following questions:
1. When will a ValueError occur? Value Error will occur when anything but a whole number is inputted.
2. When will a ZeroDivisionError occur? This will only occur when the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Enter a Integer other than 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
