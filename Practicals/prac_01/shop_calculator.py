"""CP1404 Practical
Create a calculator that the number of items can be input it and than the price of the items that
than applies a discount if total price is above 100 """

total_price = 0
number_of_items = int(input("Enter Number of Items: "))
while number_of_items < 0:
    print("Invalid number please choose another number")
    number_of_items = int(input("Enter Number of Items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item is $:"))
    total_price += price_of_item

if total_price > 100:
    total_price *= .9

print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
