print("A better solution\n")

import string
import re

name = re.compile(r'[a-zA-Z]+')  # This will check for alphabet.
your_name = input("What is your name:")  # ask the user for input.

while not name.match(your_name):
    print("invalid characters")
    your_name = input("Your Name:")
if 5 <= len(your_name) <= 10:
    print("Hi,", your_name, "!")
elif len(your_name) > 10:
    print("too long!")
elif len(your_name) < 5:
    print("too short!")
