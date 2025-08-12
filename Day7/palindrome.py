def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Ignore case and spaces
    return s == s[::-1]

# Example usage
word = input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is a Palindrome!")
else:
    print(f"{word} is not a Palindrome!")
