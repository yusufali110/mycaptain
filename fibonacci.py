# Fibonacci Series Program in Python

# Ask the user how many terms they want
n_terms = int(input("How many Fibonacci numbers would you like to print? "))

# First two terms of the Fibonacci sequence
a = 0
b = 1
count = 0

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(a)
        next_term = a + b
        # Update values
        a = b
        b = next_term
        count += 1
