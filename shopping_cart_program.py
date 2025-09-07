item = input("What do you wish to buy?: ")
price= float(input("Enter the price of the item: "))
quantity= int(input("How many would you like?: "))
total = price*quantity

print("\nShoping Cart")
print(f"Item: {item}/s")
print(f"Quantity: {quantity}")
print(f"Your total is: ${total:.2f}")
