def find_party(number):
    """Determine whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


try:
    num = int(input("Enter a number: "))
    party = find_party(num)
    print(f"The number {num} is {party}.")
except ValueError:
    print("Error: Please enter a valid integer.")

