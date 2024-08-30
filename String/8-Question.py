# Write a Python function to remove all duplicate characters from a given string.

def remove_duplicates(input_string):
    seen = set()
    result = []

    for char in input_string:
        if char not in seen:
            result.append(char)
            seen.add(char)
    
    return ''.join(result)

# Example usage
input_string = "programming"
output_string = remove_duplicates(input_string)
print(output_string)  # output ==>  "progamin"

    
    
    