# Task 1: Custom Module with Aliases

from text_utils import reverse_string as reverse, capitalize_string as capitalize

s = input("Enter the string: ")
print(f"Reversed String: {reverse(s)}")
print(f"Capitalized String: {capitalize(s)}")