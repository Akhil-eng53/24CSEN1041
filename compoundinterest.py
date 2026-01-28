import math

def get_number(msg):
    while True:
        try:
            value = float(input(msg))

            # check for invalid numbers
            if math.isnan(value) or math.isinf(value):
                print("Enter a valid finite number.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# Safe inputs
P = get_number("Enter Principal (P): ")
R = get_number("Enter Rate of Interest (R): ")
T = get_number("Enter Time in years (T): ")

# logical checks
if P < 0 or R < 0 or T < 0:
    print("Values cannot be negative.")
else:
    try:
        A = P * (1 + R/100) ** T
        CI = A - P
        print("Compound Interest:", round(CI, 2))
    except OverflowError:
        print("Numbers are too large to calculate safely.")
