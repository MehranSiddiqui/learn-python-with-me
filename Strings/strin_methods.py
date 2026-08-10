string_to_use = "This is the string we will be using"

# Get first character and last character of a string


first = string_to_use[0]
last = string_to_use[-1]

# Get substring of the string

subStr = string_to_use[0:5]
# This will return the sub string of length 5, if we will not add the starting index it will default to 0, ~ly if we donot add the ending index it will default to -1 which is the last index

# STRING METHODS

# uppercase

u_case = string_to_use.upper()

# lowercase
l_case = string_to_use.lower()

# title
title_string = string_to_use.title()
# Length

string_length = len(string_to_use)  # Can be used on any data type in python

# find
# Provides the index of first instance
find_index_of_char = string_to_use.find("h")

# replace
# Replaces the character with replacement takes two args What to replace and with what to replace

replace_string_char = string_to_use.replace("T", "J")

# To see if character or word exists in string

is_for_present = "we" in string_to_use
is_not_present = "not" in string_to_use
is_you_present = "you" not in string_to_use

print(first)
print(last)
print(subStr)
print(u_case)
print(l_case)
print(title_string)
print(string_length)
print(find_index_of_char)
print(replace_string_char)
print(is_for_present)
print(is_not_present)
print(is_you_present)