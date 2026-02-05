largest_so_far = float('-inf')
smallest_so_far = float('inf')

while True:

    numbers = input('Enter numbers: ')
    if numbers == "":
        break
    
    numbers = float(numbers)

    if largest_so_far < numbers:
        largest_so_far = numbers
    if smallest_so_far > numbers:
        smallest_so_far = numbers
    

print('The largest number is', largest_so_far)
print('The smallest number is', smallest_so_far)