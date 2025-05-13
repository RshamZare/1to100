# Palindrome Checker
# Ask the user for a word or sentence and tell them if it’s a palindrome (reads the same backward).

sentences = input("Write a word or sentence & I'll tell you if its palindrome or not: ")

if sentences == sentences[::-1]:
    print("Yes it is,", sentences[::-1])
else:
    print("No it's not :(")
