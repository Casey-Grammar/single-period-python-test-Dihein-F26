# Task 05b - Remove Duplicate Items
# Write a function called unique_items(items)
# that takes a list of strings and returns a new list with duplicates removed.
# Keep only the first occurrence of each item and preserve the original order.
#
# Example:
# unique_items(["pen", "book", "pen", "ruler", "book"])
# returns ["pen", "book", "ruler"]

def unique_items(items):
    seen = []
    
    for item in items:
        # Only add to our new list if we haven't seen it before
        if item not in seen:
            seen.append(item)
            
    return seen
    pass


def main():
    user_input = input("Enter items separated by commas: ")
    items = [item.strip() for item in user_input.split(",") if item.strip() != ""]
    print(unique_items(items))


if __name__ == "__main__":
    main()
