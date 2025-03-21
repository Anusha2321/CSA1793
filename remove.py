text = input("Enter text: ")
print("Without punctuation:", "".join(c for c in text if c.isalnum() or c.isspace()))
