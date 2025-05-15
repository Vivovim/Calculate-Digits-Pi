from decimal import Decimal, getcontext
from datetime import datetime

# Set precision
getcontext().prec = 100550  # 10,000 digits + a little buffer

def pi_digits_bbp(n):
    pi = Decimal(0)
    k = Decimal(0)
    for i in range(n):
        k = Decimal(i)
        pi += (Decimal(1) / (Decimal(16) ** k)) * (
            Decimal(4) / (8 * k + 1) -
            Decimal(2) / (8 * k + 4) -
            Decimal(1) / (8 * k + 5) -
            Decimal(1) / (8 * k + 6)
        )
    return pi

# Generate π as string
pi_val = str(pi_digits_bbp(100000))

# Split into "3" and the long decimal part
pi_whole, pi_decimal = pi_val.split(".")

# Only take first 10,000 digits from decimal part
pi_digits_only = pi_decimal[:100000]

# Prepare formatted lines
lines = []
lines.append("3.")  # Leading '3.'
for i in range(0, 100000, 76):
    lines.append(pi_digits_only[i:i+76])

# Timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d")
filename = f"100000_pi_digits_{timestamp}.txt"

# Write to file
with open(filename, "w") as f:
    for line in lines:
        f.write(line + "\n")

print(f"Done! π digits saved to: {filename}")


