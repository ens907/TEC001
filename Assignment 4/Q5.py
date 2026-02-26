def remove_uneven(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

number_list = [1, 2, 3, 4, 5, 6]
result = remove_uneven(number_list)
print("Before:", number_list)
print("After:", result)