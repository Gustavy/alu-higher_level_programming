#!/usr/bin/python3

def text_indentation(text):
 """Prints a text with 2 new lines after each of these characters: ., ?, and :

 Args:
     text: The text to be indented, must be a string.

 Raises:
     TypeError: If the input text is not a string.
 """

 if not isinstance(text, str):
   raise TypeError("text must be a string")

 # Loop through each character in the text
 for char in text:
   # Print the character without any leading or trailing spaces
   print(char, end="")

   # Check for characters requiring indentation
   if char in ".?:":
     # Print two new lines after the character
     print("\n\n", end="")

# Example usage
text = "Hello, world! This is a test. How does it look?"
text_indentation(text)