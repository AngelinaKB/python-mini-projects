# Simple Interest Calculator

# User input
principal = float(input("Enter the principal amount (₹): "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time period (in years): "))

# Calculation
interest = (principal * rate * time) / 100

# Output
print(f"\nFor ₹{principal} at {rate}% for {time} years:")
print(f"Simple Interest = ₹{interest:.2f}")
