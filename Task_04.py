# Task 04 - Expand Subject Codes
# Write a function called expand_subject_codes(codes)
# that takes a list of short subject codes and returns a new list
# with the full subject names.
#
# Use the following code table:
# ENG -> English
# MAT -> Mathematics
# SCI -> Science
# HIS -> History
# ART -> Art
#
# If a code is not recognised, ignore it.
#
# Example:
# expand_subject_codes(["MAT", "SCI", "XYZ", "ENG"])
# returns ["Mathematics", "Science", "English"]

def expand_subject_codes(codes):
    # Mapping table using a dictionary
    subject_map = {
        "ENG": "English",
        "MAT": "Mathematics",
        "SCI": "Science",
        "HIS": "History",
        "ART": "Art"
    }
    
    expanded_list = []
    
    for code in codes:
        # Only add the name if the code exists in our map
        if code in subject_map:
            expanded_list.append(subject_map[code])
            
    return expanded_list

def main():
    user_input = input("Enter subject codes separated by commas: ")
    codes = [code.strip().upper() for code in user_input.split(",") if code.strip() != ""]
    print(expand_subject_codes(codes))


if __name__ == "__main__":
    main()
