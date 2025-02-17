def is_prime(number):
    """Check if a number is a prime number."""
    if number <= 1:
        return "Is An prime Number"  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "Is Not An Prime number"  # Number is divisible by a factor other than 1 and itself
    return True

# Input from the user
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Error: Please enter a valid integer.")
