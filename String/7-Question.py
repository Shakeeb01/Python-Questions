# Write a Python function that takes two strings as input and checks if they are anagrams (contain the same characters in a different order

def are_anagrams(str1, str2):
    # Remove any whitespace and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Example usage
print(are_anagrams("shah", "hash")) 

