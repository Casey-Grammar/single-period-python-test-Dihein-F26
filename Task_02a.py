def count_vowels(text):
    # Initialize a counter
    count = 0
    # Define a string or set of vowels
    vowels = "aeiou"
    
    for char in text:
        # Check if the lowercase version of the character is a vowel
        if char.lower() in vowels:
            count += 1
            
    return count


def main():
    text = input("Enter text: ")
    print(count_vowels(text))


if __name__ == "__main__":
    main()