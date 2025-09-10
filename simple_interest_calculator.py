# Simple Interest Calculator

# User input
principal = 0
rate = 0
time = 0

# Calculation

while principal <= 0:
  principal = float(input("Enter the principal amount (₹): "))
  if principal <=0:
    print("principal can't be less than or equal to zero.")

while rate <= 0:
  rate = float(input("Enter the annual interest rate (%): "))
  if rate <=0:
    print("interest rate can't be less than or equal to zero.")
    
while time <= 0:
  time = int(input("Enter the time (in years): "))
  if rate <=0:
    print("time can't be less than or equal to zero.")
interest = (principal * rate * time) / 100

# Output
print(f"\nFor principal amount of ₹{principal} at interest rate {rate}% for {time} years:")
print(f"Simple Interest = ₹{interest:.2f}")
