# Program to find the ASCII value of the given character

c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))

# Here we have used ord() function to convert a character to an integer (ASCII value).
# This function returns the Unicode code point of that character.

# Modify the code above to get characters from their corresponding ASCII values using
# the chr() function as shown below.
# >>> chr(65)
# 'A'
# >>> chr(120)
# 'x'
# >>> chr(ord('S') + 1)
# 'T'