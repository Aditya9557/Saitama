def is_Alpha(char):
    """Determine whether a number is even or odd."""
    if char == a:
        return "Vowel"
    elif char == e:
        return "Vowel"
    elif char == i:
        return "Vowel"
    elif char == o:
        return "Vowel"
    elif char == u:
        return "Vowel"
    
    else:
        return "consotent"

try:
    char = int(input("Enter a Alphabet: "))
    party = is_Alpha(char)
    print(f"The number {char} is {Alpha}.")
except ValueError:
    print("Error: Please enter a valid Alphabet.")
