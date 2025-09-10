# Simple Interest Calculator

# User input
principal = 0
rate = 0
time = int(input("Enter the time period (in years): "))

# Calculation

while principal <= 0:
  principal = float(input("Enter the principal amount (₹): "))
  if principle <=0:
    print("principal can't be less than or equal to zero.")

while rate <= 0:
  rate = float(input("Enter the annual interest rate (%): "))
  if rate <=0:
    print("rate can't be less than or equal to zero.")
interest = (principal * rate * time) / 100

# Output
print(f"\nFor ₹{principal} at {rate}% for {time} years:")
print(f"Simple Interest = ₹{interest:.2f}")
