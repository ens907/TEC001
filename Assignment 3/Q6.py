given_string = input("Enter a string: ")

length = len(given_string)
middle = length // 2

if length % 2 == 0:
    middle_chars = given_string[middle - 1: middle + 1]
else:
    middle_chars = given_string[middle]
print("The middle characters:", middle_chars)