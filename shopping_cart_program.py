foods = []
prices = []
total = 0

while True:
  food = input("Enter a food to buy (press q to quit): ")
  if food.lower() == "q":
    break
  else:
    price =  float(input(f"Enter the price of the {foods}: $"))
    foods.append(food.capitalize())
    prices.append(price)

print("----- Your Cart -----")
for food in foods:
  print(food, end=" | ")
  
for price in prices:
  total += price

print()
print(f"Your total is: ${total:.2f}")
    

