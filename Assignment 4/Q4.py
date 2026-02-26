def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

number_list = [5, 10, 15, 20, 25]
result = sum_of_numbers(number_list)
print("The sum is:", result)