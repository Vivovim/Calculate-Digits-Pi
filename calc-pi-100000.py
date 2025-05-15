from decimal import Decimal, getcontext
from datetime import datetime

# Set precision for 100,000 digits + buffer
getcontext().prec = 100100

# Constants used in the Chudnovsky algorithm
def compute_pi_chudnovsky(n_terms):
    C = 426880 * Decimal(10005).sqrt()
    M = Decimal(1)
    L = Decimal(13591409)
    X = Decimal(1)
    K = Decimal(6)
    S = L

    for i in range(1, n_terms):
        M = (M * (K ** 3 - 16 * K)) / (Decimal(i) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    return pi

# Approx. 14 digits per term
required_digits = 100000
terms = required_digits // 14 + 10  # Add buffer for stability

# Calculate π
pi_val = str(compute_pi_chudnovsky(terms))

# Split into parts
pi_whole, pi_decimal = pi_val.split(".")
pi_digits_only = pi_decimal[:required_digits]

# Prepare formatted lines
lines = [f"{pi_whole}."]
for i in range(0, required_digits, 100):
    lines.append(pi_digits_only[i:i+100])

# Timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d")
filename = f"pi_100000_digits_{timestamp}.txt"

# Write to file
with open(filename, "w") as f:
    for line in lines:
        f.write(line + "\n")

print(f"Done! π (100,000 digits) saved to: {filename}")


