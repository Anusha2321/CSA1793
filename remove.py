text = input("Enter text: ")
print("Without punctuation:", "".join(c for c in text if c.isalnum() or c.isspace()))


#output
Enter text:  hii how are how's it going
Without punctuation:  hii how are hows it going
