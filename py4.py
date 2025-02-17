# Program to categorize a number based on its range
number = int(input("Enter a number: "))

if number < 0:
    print("The number is negative.")
elif 0 <= number < 10:
    print("The number is a single-digit positive number.")
elif 10 <= number < 100:
    print("The number is a two-digit positive number.")
elif 100 <= number < 1000:
    print("The number is a three-digit positive number.")
else:
    print("The number is a large positive number (1000 or more).")

