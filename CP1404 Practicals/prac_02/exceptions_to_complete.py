finished = False
result = 0

while not finished:
    try:
        result = int(input("Enter a Valid integer: "))
        finished = True
    except ValueError:
        print("Enter a Valid integer.")
print("Valid result is: ", result)
