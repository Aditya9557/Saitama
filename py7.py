def find_party(number):
    """Determine whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def find_square(number):
    """Calculate the square of a number."""
    return number ** 2

def find_cube(number):
    """Calculate the cube of a number."""
    return number ** 3

# Main program
try:
    print("Choose an operation:")
    print("1. Find if a number is Even or Odd")
    print("2. Find the square of a number")
    print("3. Find the cube of a number")
    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice in [1, 2, 3]:
        num = int(input("Enter a number: "))
        if choice == 1:
            result = find_party(num)
            print(f"The number {num} is {result}.")
        elif choice == 2:
            result = find_square(num)
            print(f"The square of {num} is {result}.")
        elif choice == 3:
            result = find_cube(num)
            print(f"The cube of {num} is {result}.")
    else:
        print("Error: Invalid choice. Please enter 1, 2, or 3.")
except ValueError:
    print("Error: Please enter valid numeric inputs.")
