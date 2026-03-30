def expand_subject_codes(codes):
    # 1. Define the mapping table
    subject_map = {
        "ENG": "English",
        "MAT": "Mathematics",
        "SCI": "Science",
        "HIS": "History",
        "ART": "Art"
    }
    
    # 2. Create a list to store found names
    full_names = []
    
    # 3. Iterate through the input codes
    for code in codes:
        # Check if the code exists in our dictionary
        if code in subject_map:
            full_names.append(subject_map[code])
            
    return full_names


def main():
    user_input = input("Enter subject codes separated by commas: ")
    # This line cleans up the input and handles spaces/case sensitivity
    codes = [code.strip().upper() for code in user_input.split(",") if code.strip() != ""]
    print(expand_subject_codes(codes))


if __name__ == "__main__":
    main()