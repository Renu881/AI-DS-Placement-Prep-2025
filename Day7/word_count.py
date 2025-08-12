def word_count(text):
    words = text.split()
    return len(words)

# Example usage
text_input = input("Enter a text: ")
print(f"Word Count: {word_count(text_input)}")
