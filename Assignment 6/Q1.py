numbers = []

while True:
    numbers_input = input("Enter a number: ")
    if numbers_input == "":
        break
    numbers.append(int(numbers_input))

numbers.sort(reverse=True)
five_greatest = numbers[:5]
print(five_greatest)