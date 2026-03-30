def extract_even_numbers(numbers):
    # We iterate through 'numbers' and keep 'n' only if n % 2 equals 0
    return [n for n in numbers if n % 2 == 0]


def main():
    user_input = input("Enter numbers separated by commas: ")
    # This splits the string and converts each piece into an integer
    numbers = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
    
    result = extract_even_numbers(numbers)
    print(f"Even numbers: {result}")


if __name__ == "__main__":
    main()